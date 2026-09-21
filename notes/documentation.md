# Documentation

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** Documentation / Linux Man Pages Guide (Ricardo Da Costa)  
**Logged:** 2026-09-21

## What the course covered

Linux documentation is already on the system. The manuals are called **man pages**. If you get stuck, you do not have to Google everything — you can open the page that tells you how a command works.

Man pages cover:

- How a command is used  
- Which options and arguments it needs  
- What each option means  

You do **not** have to memorise every flag. The system can teach you in place.

## How to open a man page

```bash
man <command>
```

Example from the course:

```bash
man tar
```

`tar` is an archiving utility. The page shows its synopsis and options.

## Searching inside a man page

Once a page is open:

| Key | What it does |
| --- | --- |
| `/<keyword>` | Search for a keyword (for example `/zip`) |
| `n` | Jump to the next match |
| `q` | Quit the man page |

So you stay in the terminal, look something up, and continue working.

## Man pages are not only for commands

They also document **configuration files**, so you do not have to remember every directive by heart.

```bash
man 5 crontab
```

That loads the man page for crontab **file format** — how scheduled job lines are written — not the `crontab` command itself.

**Why `5`?** Man pages are split into sections. `man man` explains them:

| Section | What it covers |
| --- | --- |
| **1** | Executable programs or shell commands |
| **5** | File formats and conventions (config files) |
| **8** | System administration commands (often root-only) |

`man man` — even the manual command has its own manual.

## What I enjoyed

I liked that you are **not forced to know everything up front**. With a lot of programming-language docs, you leave the editor, search the web, and context-switch. With `man`, the answer is **already on the terminal**.

That is useful in practice:

- Stuck on a flag? `man <command>` before you guess  
- Unsure about a config file? `man 5 <file>` when that section exists  
- Curious how `man` itself works? `man man`  

You stay in the same window. Lookup becomes part of the workflow, not a detour out of it.

## What I ran on this machine

```bash
man tar | head -15
# TAR(1) ... tar - an archiving utility

man 5 crontab | head -20
# CRONTAB(5) ... File Formats Manual — tables for driving cron

man man | head -25
# MAN(1) — interface to the system reference manuals
# Section 1 = executable programs or shell commands
```

Earlier in the shell session I also ran `man du` — same pattern: open the page, read, leave.

Re-run:

```bash
wsl -d Ubuntu
man tar
# /zip then n, q to quit
man 5 crontab
man man
```

---

*RH024 learning note — Documentation (man pages).*
