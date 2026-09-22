# Red Hat Enterprise Linux Technical Overview (RH024)

Learning notes for the free **RH024** course. Each session becomes a short note: what it covered, what I liked, what I ran.

## Notes

| Note | Session | What it covers |
| --- | --- | --- |
| [Linux distributions](notes/linux-distributions.md) | Linux Distributions Unveiled | Kernel vs distro, Fedora → CentOS Stream → RHEL, RPM vs APT, support phases, open source |
| [Introduction to the shell](notes/introduction-to-the-shell.md) | Linux Command Line Basics | Why the CLI exists, Bash default, command/options/arguments, tab completion, fish/zsh as extras |
| [Documentation](notes/documentation.md) | Linux Man Pages Guide | `man` pages, search with `/` `n` `q`, sections (1/5/8), `man 5 crontab`, staying in the terminal |
| [Command line assistant](notes/command-line-assistant.md) | RHEL Command Line Assistant / Lightspeed | AI help in the terminal (`c chat`), when it beats `man`, registration requirement |
| [Linux directories explained](notes/linux-directories-explained.md) | Linux directories explained | `/` root, `/home` `/etc` `/var` `/usr` `/tmp` `/root` `/boot`, why `/tmp` is good for testing scratch work |
| [Basic file management](notes/basic-file-management.md) | Basic file management | `ls` `mkdir` `cd` `touch` `cp` `mv` `rm`, path jumps like `cd /var/log`, fast create/delete loop |
| [Editing files with Vim](notes/editing-files-with-vim.md) | Editing files with Vim | Vim modes, `i` `Esc` `:w` `:q` `:q!` `yy` `p` `u`, VimTutor in the terminal, Vim vs nano preference |
| [Organizing local users and groups](notes/organizing-local-users-and-groups.md) | Organizing local users and groups | UIDs, `useradd`/`passwd`/`usermod`, lock vs delete, `wheel` + `sudo`, groups and least privilege, central IdM/AD |
| [File permissions](notes/file-permissions.md) | File permissions | `rwx` = 4/2/1, owner/group/other, `chmod` `chown` `chgrp`, directory vs file rules, `chmod +x` for scripts |
| [Managing software and updates](notes/managing-software-and-updates.md) | Managing software and updates | `dnf search`/`install`, RHBA/RHEA/RHSA errata, CVE + CVSS, `dnf update --security`, `dnf needs-restarting -r` |
| [Managing networking](notes/managing-networking.md) | Managing networking | Network Manager profiles, `nmcli`, `nmtui` menu path, static IPv4 example, verify with `ip` / `resolv.conf` |
| [Managing system startup services with Systemd](notes/managing-system-startup-services-with-systemd.md) | Managing Services with Systemd | units (service/socket/timer/path/target), `systemctl` start/enable/stop/disable, stop vs disable, FirewallD for httpd |
| [Deploying an application runtime](notes/deploying-an-application-runtime.md) | Deploying an application runtime | Node.js as `myapp.service`, unit file + `daemon-reload`/`enable --now`, Restart=on-failure, port 8080 + FirewallD, logs via journal |
| [Using Image Mode with Bootc](notes/using-image-mode-with-bootc.md) | Using Image Mode with Bootc | full system images, `bootc status`/`switch`/rollback, one-shot updates, transparency of what is running |
| [Insights Image Builder](notes/insights-image-builder.md) | Insights Image Builder | golden images, blueprints (only what you need), web UI at console.redhat.com, qcow2 builds |

## About this repo

Public log of what I learn in RH024. One note per session. Commands and screenshots are what I actually ran on my machine.
