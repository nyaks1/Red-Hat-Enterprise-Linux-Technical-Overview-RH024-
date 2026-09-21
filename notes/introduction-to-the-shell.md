# Introduction to the shell

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** Linux Command Line Basics / Introduction to the shell (Ricardo Da Costa)  
**Logged:** 2026-09-21

## What the course covered

One of the most powerful Linux features is the **command line**. You can manage servers remotely with more flexibility than a GUI usually gives you.

- Commands run in a **shell**.
- The **default shell on RHEL is Bash**.
- The shell’s job is to **interpret your commands**.

On the RH024 desktop the instructor opened a terminal from the Red Hat menu. Here I use Terminal / WSL / the UBI container — same idea.

## Command structure

```text
command [options] [arguments]
```

| Piece | What it is | Example |
| --- | --- | --- |
| **Command** | The program you want | `du` |
| **Options** | How it should behave (optional) | `-sh` |
| **Arguments** | What it works on | `/home/nyaks` |

Course example:

```bash
du -sh /home/rgdaCosta
```

- `du` = command (disk usage)  
- `-sh` = options (summarize + human-readable)  
- path = argument (which directory)

Options usually start with a single dash (short) or double dash (long). Some commands need options, some need arguments, some need neither. Checking the docs (`man`) before guessing saves time.

## Tab completion

**Tab** can auto-complete commands, options, and sometimes arguments.

```bash
cd /u<Tab>sh<Tab>     # → /usr
podman <Tab><Tab>     # subcommands, when the prefix is unique enough
```

If Tab does nothing, type more characters — the shell needs enough uniqueness to choose safely.

## What I enjoyed: the shell can feel faster than the GUI

I liked how direct the command line is. On my own I also looked at other shells people use besides Bash:

| Shell | Notes |
| --- | --- |
| **Bash** | RHEL default; what the course and most enterprise docs assume |
| **Zsh** | I used this on my school laptop — strong completion, comfortable for daily typing |
| **Fish** | Often feels very fast out of the box (suggestions as you type) |

**Why this is useful:** when the shell helps you finish a line (completion, history, clear output), small tasks — checking disk usage, moving through directories, reading a log — take less friction than clicking through a GUI. You can learn Bash as the default *and* still find value in what other shells improve.

RHEL itself ships with Bash as the default shell. Other shells are optional extras you can try once you are comfortable with the basics.

## What I ran on this machine

```bash
bash --version
# GNU bash, version 5.2.21(1)-release
du -sh /home/nyaks
# 19G   /home/nyaks
ls -ld /etc /usr /var
man du
```

| Result | Value |
| --- | --- |
| Shell on this WSL | Bash 5.2.21 |
| `du -sh /home/nyaks` | `19G` |
| `/etc`, `/usr`, `/var` | Present |
| `man du` | Opens docs for `du` |

Re-run:

```bash
wsl -d Ubuntu
bash --version
du -sh "$HOME"
ls -ld /etc /usr /var
man du
```

I have used zsh before on another laptop; on this machine I am working in Bash (the RHEL default) with the same kinds of commands.

---

*RH024 learning note. Course example paths use the instructor’s home (`/home/rgdaCosta`); local commands use `/home/nyaks`.*
