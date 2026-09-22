# Linux directory structure

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** Linux Directory Structure (Ricardo Da Costa)  
**Logged:** 2026-09-22

## What the course covered

When you start with Linux, the file system can feel like a maze. The idea is simple: **everything starts from one root directory**, written as a single forward slash `/`. From there, directories each have a job.

Day-to-day ones the course walked through:

| Path | What lives there |
| --- | --- |
| **`/home`** | Personal user files (for example `/home/rgdaCosta` in the course, `/home/<username>` in general). Save real work here. |
| **`/etc`** | System **configuration** files. Change how the system behaves → you are often editing under `/etc`. Backup before you change something. |
| **`/var`** | **Variable** data that changes often: logs, mail, print jobs. See what the system has been doing under `/var/log`. |
| **`/usr`** | Most installed **software**. `bin` = binaries (executables); libraries live under `/usr`; shared resources (including documentation) under `/usr/share`. |
| **`/tmp`** | **Temporary** files. Handy short-term. Linux cleans this area now and then. Every user can use `/tmp`. Do **not** store anything important there. |
| **`/root`** | Home directory of the **root** (super) user. Normal users do not get access here. |
| **`/boot`** | Kernel and files needed to start the system. |
| **`/mnt`** | Mount point for external storage. |
| **`/run`** | Temporary runtime state; cleared on reboot. |

Directories like `/dev`, `/proc`, and `/sys` are mostly system internals — the course said beginners can ignore them at first.

The course used the memory aid “extended text configurations” for **`/etc`** (think: all the config text for the system). In practice: **system configuration lives under `/etc`**.

## What I enjoyed: `/etc`, `/var`, and especially `/tmp`

Three directories stood out.

**`/etc`** — if the machine behaves differently after an edit, this is usually where the change lives. That makes the system feel understandable instead of magical.

**`/var`** — logs and other data that move over time. Useful when you want to see what a process has been doing.

**`/tmp`** — this is the one I liked most for **my own work**. When I am testing software and making changes as I go, a temporary place is exactly what I want:

- Drop throwaway files, scratch outputs, quick experiments  
- Avoid cluttering a project while a change is still in flux  
- Every user can write there on a typical system  

**Why this is useful (testing on my laptop):** iterate → write to `/tmp` → check → delete or let it get cleaned up. Real code and notes stay in my project; `/tmp` is the workbench. Rule from the course I am keeping: **do not put anything important in `/tmp`**.

## What I ran on this machine

```bash
ls /
ls -ld /home /etc /var /tmp /usr /boot
ls /var
echo 'rh024-tmp-test' > /tmp/nyaks-tmp-demo.txt
cat /tmp/nyaks-tmp-demo.txt
```

That last pair is the habit in miniature: scratch file in `/tmp`, read it back, throwaway.

Re-run:

```bash
wsl -d Ubuntu
ls /
ls -ld /etc /var /tmp
echo test > /tmp/demo.txt && cat /tmp/demo.txt
```

---

*RH024 learning note — Linux directory structure.*
