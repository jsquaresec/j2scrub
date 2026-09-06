from __future__ import annotations
import os
import platform
import shutil
import subprocess
import tempfile
from pathlib import Path
from j2scrub.models import Action, Report


def _candidate_paths() -> list[tuple[str, Path]]:
    home = Path.home()
    items: list[tuple[str, Path]] = []
    system = platform.system().lower()
    if system == "linux":
        items += [
            ("bash_history", home / ".bash_history"),
            ("zsh_history", home / ".zsh_history"),
            ("thumbnails", home / ".cache" / "thumbnails"),
        ]
    elif system == "windows":
        local = Path(os.environ.get("LOCALAPPDATA", home))
        appdata = Path(os.environ.get("APPDATA", home))
        items += [
            ("powershell_history", appdata / "Microsoft" / "Windows" / "PowerShell" / "PSReadLine" / "ConsoleHost_history.txt"),
            ("recent_items", appdata / "Microsoft" / "Windows" / "Recent"),
            ("thumbnail_cache", local / "Microsoft" / "Windows" / "Explorer"),
        ]
    items.append(("temp_directory", Path(tempfile.gettempdir())))
    return items


def preview() -> Report:
    report = Report()
    for kind, path in _candidate_paths():
        if path.exists():
            report.actions.append(Action(kind, path, f"Clean {kind.replace('_', ' ')}", True))
    report.actions.append(Action("clipboard", "system clipboard", "Clear clipboard contents", True))
    return report


def _clear_clipboard() -> bool:
    system = platform.system().lower()
    try:
        if system == "windows":
            subprocess.run(["powershell", "-NoProfile", "-Command", "Set-Clipboard -Value $null"], check=False, capture_output=True)
            return True
        for cmd in (["wl-copy", "--clear"], ["xclip", "-selection", "clipboard", "/dev/null"]):
            if shutil.which(cmd[0]):
                subprocess.run(cmd, check=False, capture_output=True)
                return True
    except OSError:
        return False
    return False


def execute(actions: list[Action]) -> list[str]:
    results: list[str] = []
    for action in actions:
        if action.kind == "clipboard":
            results.append("clipboard: cleared" if _clear_clipboard() else "clipboard: no supported clipboard command found")
            continue
        path = Path(action.target)
        try:
            if path.is_dir():
                for child in path.iterdir():
                    try:
                        if child.is_dir():
                            shutil.rmtree(child)
                        else:
                            child.unlink()
                    except OSError:
                        pass
                results.append(f"{action.kind}: cleaned")
            elif path.is_file():
                path.write_text("", encoding="utf-8")
                results.append(f"{action.kind}: cleared")
        except OSError as exc:
            results.append(f"{action.kind}: skipped ({exc})")
    return results
