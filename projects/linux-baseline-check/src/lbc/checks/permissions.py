"""Permission checks — world-writable files and scripts missing +x."""

from __future__ import annotations

import os
import stat


def scan(path: str) -> list[str]:
    findings: list[str] = []
    root = os.path.abspath(path)
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            full = os.path.join(dirpath, name)
            try:
                mode = os.lstat(full).st_mode
            except OSError:
                continue
            if not stat.S_ISREG(mode):
                continue
            if mode & stat.S_IWOTH:
                findings.append(f"[permissions]  {full}  world-writable")
            # scripts: shebang but no execute bit
            try:
                with open(full, "rb") as f:
                    head = f.read(2)
            except OSError:
                continue
            if head == b"#!" and not mode & stat.S_IXUSR:
                findings.append(f"[permissions]  {full}  shebang but not executable")
    return findings
