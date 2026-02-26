"""EnvBench to Harbor task format adapter.

Converts EnvBench (Python) benchmark tasks from HuggingFace into
Harbor-compatible task directories.
"""

import json
import logging
import os
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

TEMPLATES_DIR = Path(__file__).parent / "templates"


@dataclass
class EnvBenchRecord:
    repository: str
    revision: str


@dataclass
class HarborTaskPaths:
    root: Path

    @property
    def task_toml(self) -> Path:
        return self.root / "task.toml"

    @property
    def instruction_md(self) -> Path:
        return self.root / "instruction.md"

    @property
    def dockerfile(self) -> Path:
        return self.root / "environment" / "Dockerfile"

    @property
    def test_sh(self) -> Path:
        return self.root / "tests" / "test.sh"

    @property
    def solve_sh(self) -> Path:
        return self.root / "solution" / "solve.sh"

    @property
    def config_json(self) -> Path:
        return self.root / "tests" / "config.json"

    def create_dirs(self) -> None:
        for subdir in ["environment", "tests", "solution"]:
            (self.root / subdir).mkdir(parents=True, exist_ok=True)


def make_task_id(record: EnvBenchRecord) -> str:
    """Generate a Harbor task ID from an EnvBench record."""
    owner, name = record.repository.split("/", 1)
    return f"{owner}-{name}-{record.revision[:8]}"


def _read_template(name: str) -> str:
    return (TEMPLATES_DIR / name).read_text()


def generate_task(record: EnvBenchRecord, output_dir: Path, overwrite: bool = False) -> Optional[Path]:
    """Generate a single Harbor task directory from an EnvBench record.

    Returns the task directory path on success, None on failure.
    """
    task_id = make_task_id(record)
    task_dir = output_dir / task_id
    paths = HarborTaskPaths(root=task_dir)

    if task_dir.exists():
        if not overwrite:
            logger.info(f"Skipping {task_id} (already exists)")
            return task_dir
        shutil.rmtree(task_dir)

    paths.create_dirs()

    fmt = {"repository": record.repository, "revision": record.revision}

    # task.toml
    paths.task_toml.write_text(_read_template("task.toml").format(**fmt))

    # instruction.md
    paths.instruction_md.write_text(_read_template("instruction.md").format(**fmt))

    # environment/Dockerfile
    paths.dockerfile.write_text(_read_template("Dockerfile").format(**fmt))

    # tests/test.sh — no placeholders, copy as-is
    paths.test_sh.write_text(_read_template("test.sh"))
    paths.test_sh.chmod(0o755)

    # solution/solve.sh — no placeholders, copy as-is
    paths.solve_sh.write_text(_read_template("solve.sh"))
    paths.solve_sh.chmod(0o755)

    # tests/config.json — raw record for reference
    paths.config_json.write_text(json.dumps({"repository": record.repository, "revision": record.revision}, indent=2))

    logger.info(f"Generated task: {task_id}")
    return task_dir


def generate_many(
    records: list[EnvBenchRecord],
    output_dir: Path,
    overwrite: bool = False,
) -> dict[str, list[str]]:
    """Generate Harbor tasks for multiple EnvBench records.

    Returns a dict with 'success' and 'failed' task IDs.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    results: dict[str, list[str]] = {"success": [], "failed": []}

    for record in records:
        task_id = make_task_id(record)
        try:
            path = generate_task(record, output_dir, overwrite=overwrite)
            if path:
                results["success"].append(task_id)
        except Exception:
            logger.exception(f"Failed to generate task {task_id}")
            results["failed"].append(task_id)

    logger.info(f"Generated {len(results['success'])} tasks, {len(results['failed'])} failed")
    return results
