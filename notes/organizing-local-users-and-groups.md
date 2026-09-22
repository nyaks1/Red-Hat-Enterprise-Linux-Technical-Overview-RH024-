# Organizing local users and groups

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** Organizing local users and groups / User and Group Management (Ricardo Da Costa)  
**Logged:** 2026-09-22

Long session — it opened with a **Remember…** back to `/etc` and built from there.

## What the course covered

### Where accounts live

Remember [Linux directories explained](linux-directories-explained.md): **`/etc`** holds configuration — including the **local user and group databases**.

- `/etc/passwd` — account names, UIDs, home directories, shells (despite the name, **not** password hashes)  
- Passwords live in a more protected file (typically `/etc/shadow`)  
- `/etc/group` — group names and membership  

Local users fit **standalone servers, lab machines, and small setups**. In bigger shops, people are usually managed in a **central identity provider** (Active Directory, or Red Hat **IdM** — Identity Management). Day-to-day logins then come from that centre; local accounts still matter for recovery and system work.

### Users and UIDs

| Command | Job |
| --- | --- |
| `useradd` | Create a local user (needs admin / `sudo`) |
| `passwd` | Set a password |
| `usermod` | Change a user (shell, groups, etc.) |
| `userdel` | Delete a user (home dir only with `-r`) |
| `id` | Show UID, GID, and groups |
| `groups` | Show group membership |

Every account has a **UID** (user ID). When you **onboard** someone, `useradd` creates the account and home directory; `passwd` sets their password.

**Demo warning from the course:** a weak password like `RedHat` is shorter than 8 characters and common in password lists — root can set it, but that does not make it a good password.

### Deleting users is a security problem (UID reuse)

The instructor’s story is the part worth keeping:

1. Create **Allison** → she gets a UID (e.g. 1001).  
2. Delete Allison’s account (`userdel`) but **keep her home directory** (sometimes required for data retention).  
3. Create **Mo** → system hands out the **next free UID**, which may be **the freed 1001**.  
4. Result: **Mo can end up owning Allison’s old files.** Accidental access to someone else’s data.

Safer habits from the session:

- Prefer **locking** an account over deleting (`passwd -l` / unlock with `passwd -u`) — files and audit history stay, login is blocked  
- If you must remove an account, **find their files first** (`find` by UID), then archive or securely delete before the account goes away  
- `userdel -r` removes the home directory too — only when policy allows  

### Groups and privileges

Groups are how you give **roles**, not how you make everyone equal.

- `groupadd` / `groupmod` / `groupdel` manage groups  
- `usermod -aG <group> <user>` adds someone to a group  
- `id Curtis` / `groups Curtis` show where they sit  

**`wheel`** is the default admin group on RHEL: only people in `wheel` should use **`sudo`** for elevated work. Red Hat’s point: only trusted users make critical system changes.

### `sudo` vs `su` (and why it matters)

| Approach | What happens | Why it matters |
| --- | --- | --- |
| **`sudo`** | Run **one** command as root (or `sudo -i` for a root shell) | Safer default; **audited** — trail of who ran what |
| **`su`** | Switch to another user (`su -` = full root login with **root password**) | Orgs rarely share root’s password; if everyone logs in as root, **you lose who did what** |

Preferred framework for **traceability and safety**: `sudo`. Only `wheel` members, per-command elevation, audit trail.

## What I enjoyed

This one was a mouthful — but it clicked for me as **cybersecurity-shaped thinking**, not just “Linux homework.”

On my personal PC I am effectively **everyone**: one human, full power, almost no walls. The course showed how **risky** that is once more than one person (or one role) exists:

> You do not want the sales person to have the IT person’s permissions.

**Groups** are the fix. Everyone works with **what they are allowed to do** and nothing more. That is least privilege in plain clothes.

I also liked the **onboarding + UID** story. Creating an admin is not only “add a username.” It is identity (UID), home directory, groups, password, and later **offboarding that does not leak someone else’s files** because a number got reused.

**Why this is useful:** whether I end up in security, infra, or shipping apps on Linux servers, access control is the boring core. Sales ≠ IT. Contractor ≠ admin. Locked accounts and audit trails are how you sleep at night.

## What I ran on this machine

Read-only identity check (WSL — no new users created):

```bash
id
# uid=1000(nyaks) ... groups=... sudo ... docker
groups
grep -E '^(root|nyaks):' /etc/passwd
# root:x:0:0:root:/root:/bin/bash
# nyaks:x:1000:1000:...:/home/nyaks:/usr/bin/zsh
```

That is onboarding in one line: **UID 1000**, home `/home/nyaks`, login shell `/usr/bin/zsh`, and membership in **`sudo`** (RHEL’s equivalent would be **`wheel`**).

Re-run the course pattern on a lab VM when you have admin rights:

```bash
sudo useradd allison
sudo passwd allison
id allison
sudo passwd -l allison          # lock — safer than delete
sudo find / -uid 1001 2>/dev/null
```

---

*RH024 learning note — Organizing local users and groups.*
