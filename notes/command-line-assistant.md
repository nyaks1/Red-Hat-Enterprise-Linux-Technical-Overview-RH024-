# Command line assistant

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** RHEL Command Line Assistant / RHEL Lightspeed (Ricardo Da Costa)  
**Logged:** 2026-09-22

## What the course covered

RHEL 10 adds a **Command Line Assistant** — AI help **in the terminal**, connected to **RHEL Lightspeed**. The idea is a Linux expert available where you already work, so you do not have to switch windows to search the web when you are stuck.

From the course:

- Ask in natural language instead of only looking up flags  
- Example style of use: type `c chat` and your question  
- The assistant replies in the terminal and keeps you in that workspace  

There is one catch they were clear about: the system needs to be **registered** before the Command Line Assistant is available. Registration is also how systems get updates and related features. They showed `subscription-manager` for registering with Red Hat’s content delivery network, or a company **Satellite** server if your org mirrors Red Hat software internally.

## How it fits next to `man`

| Tool | Best when… |
| --- | --- |
| **`man`** | You know the command and need options, file format, or exact syntax |
| **Command line assistant** | You know **what you want to do** but cannot remember **which command** (or how to phrase it) |

`man tar` tells you how `tar` works. The assistant is for the moment before that — when you are thinking “how do I archive this directory?” and do not want to leave the terminal to find `tar` first.

## What I enjoyed

I liked that it feels like a **better version of the man command** for the blank-page case. Sometimes you know the job but not the command name. Typing `c chat` and the question keeps help **in the terminal**, like man pages, but from the other direction:

- **man** = I have the name, give me the truth  
- **assistant** = I have the intent, give me the name / next step  

Staying on the command line is still the point. The AI does not replace learning the commands; it shortens the path back to them.

## Why this is useful

- Less context-switching than a browser tab for “what was that command?”  
- Good for recalling options, flags, or common admin tasks under pressure  
- Still built around the same terminal workflow as `man`, tab completion, and Bash  

Practical habit: ask the assistant for a starting command, then `man` that command before you run anything important. Intent → command → documentation → execute.

## What I can run here

On this machine I am in WSL / UBI for RH024 work — not a registered RHEL 10 desktop — so the Command Line Assistant is not something I have used locally yet. What I *did* practise is the same “don’t memorise everything” path with the tools I have:

```bash
man tar
man 5 crontab
man man
```

When I am on a registered RHEL 10 system, the course pattern is:

```text
c chat <question>
```

Example from the session style: ask something like *Why should I register RHEL?* and read the answer without leaving the terminal.

---

*RH024 learning note — Command line assistant (RHEL Lightspeed).*
