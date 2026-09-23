"""lbc command-line entry."""

from __future__ import annotations

import argparse
import sys

from . import __version__
from .checks import permissions, services, updates, users


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="lbc", description="linux-baseline-check")
    parser.add_argument("--version", action="version", version=f"lbc {__version__}")
    sub = parser.add_subparsers(dest="cmd", required=True)

    scan = sub.add_parser("scan", help="run local baseline checks")
    scan.add_argument("--path", default=".", help="path for file checks (default: .)")

    args = parser.parse_args(argv)
    if args.cmd == "scan":
        findings: list[str] = []
        print(f"lbc — linux-baseline-check v{__version__}")
        findings.extend(permissions.scan(args.path))
        findings.extend(users.scan(args.path))
        findings.extend(services.scan(args.path))
        findings.extend(updates.scan(args.path))
        for line in findings:
            print(line)
        print(f"{len(findings)} findings")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
