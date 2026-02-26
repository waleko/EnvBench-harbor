# Environment Setup Task

You are working inside a Docker container with a cloned GitHub repository.

**Repository:** `artesiawater/hydropandas`
**Commit:** `2426022ead74875a5f5abf6830c405d07533e78c`

## Objective

Write and execute a bash script that correctly sets up the Python development environment for this repository so that all dependencies are installed and importable.

## Environment

The container has the following tools pre-installed:
- **pyenv** with Python versions: 3.8.18, 3.9.18, 3.10.13, 3.11.7, 3.12.0, 3.13.1
- **conda** (Miniconda)
- **poetry**
- **uv**
- **pipenv**
- Standard build tools (gcc, make, etc.)

The repository is located at `/data/project`.

## Requirements

1. Detect the correct Python version for this project
2. Set up the appropriate Python environment (virtualenv, conda env, etc.)
3. Install all project dependencies
4. Ensure all Python imports resolve correctly

## Evaluation

Your setup will be verified by running **pyright** to check for `reportMissingImports` errors. A successful setup results in zero missing import errors.

## Output

Write your setup script to `/data/project/bootstrap_script.sh` and execute it.
