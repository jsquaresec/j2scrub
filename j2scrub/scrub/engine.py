from __future__ import annotations
import shutil
from pathlib import Path
from j2scrub.models import Report
from j2scrub.scrub.images import inspect_image, sanitize_image
from j2scrub.scrub.secrets import scan_text_file


def _walk(target: Path):
    if target.is_file():
        yield target
    elif target.is_dir():
        for p in target.rglob("*"):
            if p.is_file():
                yield p


def scan(target: Path) -> Report:
    report = Report()
    for path in _walk(target):
        report.extend(scan_text_file(path))
        report.extend(inspect_image(path))
    return report


def sanitize(target: Path, output: Path) -> Report:
    report = scan(target)
    if target.is_file():
        if target.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}:
            sanitize_image(target, output)
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, output)
        return report

    output.mkdir(parents=True, exist_ok=True)
    for source in _walk(target):
        rel = source.relative_to(target)
        dest = output / rel
        if source.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}:
            sanitize_image(source, dest)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
    return report
