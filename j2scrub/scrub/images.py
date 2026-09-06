from __future__ import annotations
from pathlib import Path
from PIL import Image
from j2scrub.models import Action, Finding, Report

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}


def inspect_image(path: Path) -> Report:
    report = Report()
    if path.suffix.lower() not in IMAGE_SUFFIXES:
        return report
    try:
        with Image.open(path) as img:
            exif = img.getexif()
            if exif and len(exif):
                report.findings.append(Finding("metadata", f"Image contains {len(exif)} EXIF metadata field(s)", "medium", path))
                report.actions.append(Action("sanitize_image", path, "Create a metadata-stripped copy"))
    except Exception:
        report.findings.append(Finding("image_error", "Could not inspect image metadata", "low", path))
    return report


def sanitize_image(path: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(path) as img:
        clean = Image.new(img.mode, img.size)
        clean.putdata(list(img.getdata()))
        save_kwargs = {}
        if img.format:
            save_kwargs["format"] = img.format
        clean.save(output, **save_kwargs)
