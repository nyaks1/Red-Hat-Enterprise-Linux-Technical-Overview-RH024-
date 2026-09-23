# linux-baseline-check

**linux-baseline-check** is a small CLI that scans a Linux system (or UBI container) for risky configuration — file permissions, leftover user IDs, services enabled at boot, and outdated packages — and prints a short, readable report.

Unlike generic mega-auditors, we stay **teachable and scoped**: a few high-signal checks from everyday Linux admin (users, permissions, systemd, packages). Built for students and small teams who want a clear report, not another enterprise dashboard.

## What we do (v1)

| Check | Question it answers |
| --- | --- |
| **permissions** | World-writable files? Scripts without execute? Odd modes on `/tmp` demos? |
| **users** | Shared/odd UIDs? Accounts that look deleted but left files? |
| **services** | What is enabled at boot? Anything surprising in `multi-user.target`? |
| **updates** | Packages that look outdated (via `rpm`/`dpkg` where available)? |

## What we do **not** do

- No cloud account required  
- No agent, no phone-home, no “AI SOC”  
- No claim to replace SELinux, OpenSCAP, or Red Hat Insights  
- No collection of personal file **contents** (metadata only: modes, UIDs, unit names, package names)

## Quick demo (target v0.1)

```bash
python -m lbc scan --path /tmp/demo
```

```text
lbc — linux-baseline-check
[permissions]  /tmp/demo/run.sh  mode 666  world-writable
[permissions]  /tmp/demo/tool.sh  not executable
[users]        (stub)
[services]     (stub)
[updates]      (stub)
3 findings
```

## Install (dev)

```bash
cd linux-baseline-check
python -m venv .venv
. .venv/bin/activate
pip install -e .
lbc --help
```

## Roadmap

- [x] Repo + pitch + scope  
- [ ] `lbc scan` stub  
- [ ] permissions check (real)  
- [ ] users / services / updates  
- [ ] JSON + markdown report  
- Later: **lab bootstrap** tool (first 10 minutes on a RHEL/UBI VM)

## License

Open source (see `LICENSE`) — read it, change it, share improvements.
