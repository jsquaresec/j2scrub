from __future__ import annotations
import re
from pathlib import Path
from j2scrub.models import Finding, Report

PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,255}\b"),
    "jwt": re.compile(r"\beyJ[a-zA-Z0-9_-]{8,}\.[a-zA-Z0-9_-]{8,}\.[a-zA-Z0-9_-]{8,}\b"),
    "generic_secret": re.compile(r"(?i)\b(api[_-]?key|token|secret|password)\b\s*[:=]\s*[\"']?([^\s\"']{8,})"),
}

TEXT_SUFFIXES = {".txt", ".log", ".md", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env", ".py", ".js", ".ts", ".sh", ".ps1"}


def scan_text_file(path: Path) -> Report:
    report = Report()
    if path.suffix.lower() not in TEXT_SUFFIXES and path.name != ".env":
        return report
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return report
    for kind, pattern in PATTERNS.items():
        if pattern.search(text):
            report.findings.append(Finding(kind, f"Potential {kind.replace('_', ' ')} detected", "high", path))
    if re.search(r"(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)", text):
        report.findings.append(Finding("ip_address", "IPv4 address detected", "info", path))
    if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text):
        report.findings.append(Finding("email", "Email address detected", "info", path))
    return report
