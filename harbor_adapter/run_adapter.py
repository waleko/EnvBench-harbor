"""CLI entry point for converting EnvBench tasks to Harbor format.

Usage:
    uv run generate --output-dir ./out
    uv run generate --output-dir ./out --limit 10
"""

import argparse
import logging
from pathlib import Path

from datasets import load_dataset

from harbor_adapter.adapter import EnvBenchRecord, generate_many

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_HF_REPO = "JetBrains-Research/PIPer-envbench-zeroshot-rl"


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert EnvBench tasks to Harbor task format")
    parser.add_argument("--output-dir", type=Path, required=True, help="Output directory for Harbor tasks")
    parser.add_argument("--hf-repo", type=str, default=DEFAULT_HF_REPO, help="HuggingFace dataset repo ID")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of tasks per split")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing task directories")
    args = parser.parse_args()

    logger.info(f"Loading dataset {args.hf_repo}")
    ds = load_dataset(args.hf_repo)

    total_success = 0
    total_failed = 0

    for split in ds:
        records = []
        for i, item in enumerate(ds[split]):
            if args.limit and i >= args.limit:
                break
            records.append(EnvBenchRecord(repository=item["repository"], revision=item["revision"]))

        logger.info(f"[{split}] Loaded {len(records)} tasks")

        output_dir = args.output_dir / split
        results = generate_many(records, output_dir, overwrite=args.overwrite)

        total_success += len(results["success"])
        total_failed += len(results["failed"])

        logger.info(f"[{split}] {len(results['success'])} succeeded, {len(results['failed'])} failed")
        if results["failed"]:
            logger.warning(f"[{split}] Failed: {results['failed']}")

    logger.info(f"Total: {total_success} succeeded, {total_failed} failed")


if __name__ == "__main__":
    main()
