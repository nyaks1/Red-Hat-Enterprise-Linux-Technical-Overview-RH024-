# Introduction to the shell

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** Linux Command Line Basics / Introduction to the shell (Ricardo Da Costa)  
**Logged:** 2026-09-21  
**Repo trail:** second unit after [Linux distributions](linux-distributions.md)

## What the course covered

One of the most powerful Linux features is the **command line**. It is not there because Linux is old — it is there because operators need to manage servers **remotely**, with flexibility a GUI often cannot match.

- Commands run in a **shell**.
- The **default shell on RHEL is Bash**.
- The shell’s job is simple to say: **interpret your commands**.

On the RH024 desktop, the instructor opened a terminal via the Red Hat logo → terminal icon. In our world it is Terminal / WSL / UBI — same idea, different door.

## Command structure (the grammar you must own)

```text
command [options] [arguments]
```

| Piece | What it is | Example |
| --- | --- | --- |
| **Command** | The program you want | `du` |
| **Options** | How it should behave; optional; `-s` / `--summarize` style | `-sh` |
| **Arguments** | What it works on (file, directory, target) | `/home/nyaks` |

Course example:

```bash
du -sh /home/rgdaCosta
```

- `du` = command (disk usage)  
- `-sh` = options (summarize + human-readable)  
- path = argument (which directory)

Options usually start with a **single dash** (short) or **double dash** (long). Some commands need options, some need arguments, some need neither, some need both. **Read the documentation** before you guess.

## Tab completion

One of the shell’s highest-value habits: **Tab** auto-completes commands, options, and sometimes arguments.

Course moves:

```bash
cd /u<Tab>sh<Tab>     # → /usr  (path completion)
podman <Tab><Tab>     # list subcommands when unique enough
```

If Tab does nothing, the shell needs **more uniqueness** — type another character, Tab again. That is not the shell being rude; it is refusing to guess.

## What I liked: the shell feels faster than the GUI (fish / zsh)

The course default is Bash. I went one step further on my own time and looked at other shells people swear by:

| Shell | Why people like it |
| --- | --- |
| **Bash** | RHEL default, every cert/lab assumes it, docs everywhere |
| **Zsh (zsh)** | Flexible, strong completion/themes culture, still “serious” for many devs |
| **Fish** | Opinionated and friendly out of the box — smart suggestions, autosuggestions, often *feels* fast |

For me the pull is simple: when the shell starts helping you finish the line, it feels **more comfortable and faster than clicking through a GUI**. Open source again — the interface is not sacred. You can keep Bash as the system language and still learn what other shells change.

**Mentor honesty (for future me):** RH024, RHCSA-style work, and enterprise RHEL assume **Bash**. Fish/zsh can make *my* typing nicer; they do not replace Bash muscle memory. Learn the default first. Customize second. Don’t show up to a lab unable to drive `/bin/bash`.

## Hands-on (this machine)

Environment checked on WSL Ubuntu + prior UBI work:

```bash
bash --version
# GNU bash, version 5.2.21(1)-release
du -sh /home/nyaks
# 19G   /home/nyaks
ls -ld /etc /usr /var
man du   # documentation before guessing
```

| Result | Value |
| --- | --- |
| Shell on this WSL | Bash 5.2.21 |
| `fish` / `zsh` installed here | **Not present yet** — curiosity only until I install and compare |
| `du -sh /home/nyaks` | `19G` |
| FHS paths | `/etc`, `/usr`, `/var` exist |
| Docs | `man du` works — check before inventing flags |

### Re-run

```bash
wsl -d Ubuntu
bash --version
du -sh "$HOME"
ls -ld /etc /usr /var
man du
```

Optional (when I actually want the fish/zsh comparison, not just the idea):

```bash
sudo apt update && sudo apt install -y zsh
# fish only if/when I choose to; Ubuntu package name: fish
zsh --version
```

## Checklist

- [x] Watch RH024 shell / command line session (2026-09-21)
- [x] Write this note with command anatomy + tab completion
- [x] Run `du` / `ls` / `man` evidence on this machine
- [x] Note fish/zsh as personal exploration — not RHEL default
- [ ] Use Tab completion deliberately in a real session (paths + subcommands)
- [ ] Install zsh/fish only after Bash habits are solid — then compare, don’t cosplay
- [ ] (Carried) Confirm no-cost RHEL developer subscription
- [ ] (Carried) Boot ISO in a VM + `subscription-manager list --consumed`

## Standing gates

- **Brand fit:** CLI fluency is foundation for Cybersecurity, FinTech infra, later Flutter backends — hours count.
- **Shovel:** the shell is the shovel. GUIs are the storefront.
- **POPIA:** public notes only; no credentials; no personal data in screenshots.
- **Build the man:** fast typing is vanity if you can’t explain `command options arguments`.

---

*RH024 learning note. Course example paths use the instructor’s home (`/home/rgdaCosta`); local evidence uses `/home/nyaks`. Default shell on RHEL remains Bash.*
