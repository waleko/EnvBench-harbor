#!/bin/bash

# Do NOT use set -e — the bootstrap script may fail, and we must always write rewards.

# Create output directories
mkdir -p /logs/verifier build_output
chmod -R 777 .

# Initialize results
printf '{"pyright": {}}\n' > build_output/results.json

# If the agent produced a bootstrap script, run it (ignore failures)
if [ -f "./bootstrap_script.sh" ]; then
  echo "Bootstrap script contents:"
  cat ./bootstrap_script.sh
  echo "Running bootstrap script..."
  source ./bootstrap_script.sh || echo "WARNING: bootstrap script exited with code $?"
fi

# Check that jq is installed
if ! command -v jq &> /dev/null; then
    echo "jq not found"
    echo "0" > /logs/verifier/reward.txt
    echo '{"issues_count": -1, "exit_code": 1, "error": "jq not found"}' > /logs/verifier/reward.json
    exit 0
fi

# Install pyright
python -m pip install --quiet pyright || true

# Print which Python is being used
echo "Using $(python --version 2>&1) located at $(which python 2>/dev/null || echo 'not found')"

# Run type checking with pyright
echo "Running type checks..."

# Run pyright and capture output regardless of exit code
python -m pyright /data/project --level error --outputjson > build_output/pyright_output.json 2>&1 || true

# Check if pyright output exists and is valid JSON
if [ ! -f build_output/pyright_output.json ] || ! jq empty build_output/pyright_output.json 2>/dev/null; then
    echo "Failed to get valid pyright output"
    echo "0" > /logs/verifier/reward.txt
    echo '{"issues_count": -1, "exit_code": 1, "error": "pyright output missing or invalid"}' > /logs/verifier/reward.json
    exit 0
fi

# Count only critical import issues (reportMissingImports)
issue_count=$(jq '[.generalDiagnostics[] | select(.rule == "reportMissingImports")] | length' \
    build_output/pyright_output.json 2>/dev/null || echo "-1")

echo "Found $issue_count missing import issues"

# Write binary reward: 1.0 if zero issues, 0.0 otherwise
if [ "$issue_count" = "0" ]; then
    echo "1" > /logs/verifier/reward.txt
else
    echo "0" > /logs/verifier/reward.txt
fi

# Write detailed metrics to reward.json
jq -n --argjson issues "${issue_count:--1}" \
    '{"issues_count": $issues}' > /logs/verifier/reward.json

chmod -R 777 .
exit 0
