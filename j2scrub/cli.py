from __future__ import annotations
import argparse
from pathlib import Path
from j2scrub import __version__
from j2scrub.scrub.engine import scan, sanitize
from j2scrub.burn.engine import preview, execute


def _print_report(report):
    if report.findings:
        print("Findings:")
        for f in report.findings:
            where = f" [{f.path}]" if f.path else ""
            print(f"  - {f.severity.upper():6} {f.message}{where}")
    if report.actions:
        print("Actions:")
        for a in report.actions:
            print(f"  - {a.description}: {a.target}")
    if not report.findings and not report.actions:
        print("No findings.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="j2scrub", description="Sanitize what you share. Burn what you leave behind.")
    parser.add_argument("--version", action="version", version=f"j2scrub {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    scan_p = sub.add_parser("scan", help="Scan a file or directory for metadata and secrets")
    scan_p.add_argument("target", type=Path)

    scrub_p = sub.add_parser("scrub", help="Create a sanitized copy")
    scrub_p.add_argument("target", type=Path)
    scrub_p.add_argument("--output", "-o", type=Path)

    burn_p = sub.add_parser("burn", help="Preview or execute local trace cleanup")
    burn_p.add_argument("--apply", action="store_true", help="Actually perform cleanup. Without this flag, burn is dry-run only.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "scan":
        _print_report(scan(args.target))
        return 0
    if args.command == "scrub":
        output = args.output
        if output is None:
            output = args.target.with_name(args.target.stem + ".scrubbed" + args.target.suffix) if args.target.is_file() else args.target.with_name(args.target.name + "-scrubbed")
        report = sanitize(args.target, output)
        _print_report(report)
        print(f"Sanitized copy: {output}")
        return 0
    if args.command == "burn":
        report = preview()
        _print_report(report)
        if not args.apply:
            print("Dry run only. Re-run with --apply to execute these cleanup actions.")
            return 0
        print("Results:")
        for line in execute(report.actions):
            print(f"  - {line}")
        return 0
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
