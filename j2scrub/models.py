from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class Finding:
    kind: str
    message: str
    severity: str = "info"
    path: Path | None = None

@dataclass
class Action:
    kind: str
    target: Path | str
    description: str
    destructive: bool = False

@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)
    actions: list[Action] = field(default_factory=list)

    def extend(self, other: "Report") -> None:
        self.findings.extend(other.findings)
        self.actions.extend(other.actions)
