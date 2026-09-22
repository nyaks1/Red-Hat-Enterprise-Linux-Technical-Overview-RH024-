# Editing files with Vim

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** Editing files with Vim / Vim Basics for Editing (Ricardo Da Costa)  
**Logged:** 2026-09-22

## What the course covered

Vim is a text editor you will find on almost every Linux install. It is **fast**, **lightweight**, and usually already there when you need to edit a file — including on a remote server.

People hear “scary stories” about Vim. The course point: once you have the **basics**, it is powerful and not that strange. Learn open, edit, save, quit first. Fancy features can wait.

### Modes

| Mode | What it is for |
| --- | --- |
| **Normal** | Move around and run commands (you start here) |
| **Insert** | Actually typing text (`i` at the cursor; the screen shows `-- INSERT --`) |
| **Command** | Save, quit, search — start with `:` from normal mode |

```bash
vim myfile.txt
```

### Basics from the session

| Keys | What they do |
| --- | --- |
| `i` | Enter **insert** mode at the cursor |
| `Esc` | Back to **normal** mode |
| `:` | Command mode (from normal) |
| `:w` | Write (save) |
| `:q` | Quit |
| `:wq` / `:x` | Save and quit |
| `:q!` | Quit **without** saving |
| `yy` | Copy (yank) a line |
| `p` | Paste |
| `10p` | Paste the same text ten times |
| `u` | Undo |
| `Ctrl+r` | Redo |

You cannot save from insert mode — `Esc` first, then `:w`. Keystrokes in normal mode are **commands**, not letters in the file.

### VimTutor

The course pushed **VimTutor** — an interactive tutorial **in the terminal**:

```bash
vimtutor
```

It teaches Vim *while you stay in Vim/the terminal*.

## What I enjoyed

I have used **nano** before. Vim is still my favourite — maybe preference, maybe the way it sits under your fingers once the modes click. Either way I was happy to learn it properly.

The line that stuck: **the interactive tutorial lives in the terminal too** (`vimtutor`). With `man` you *look up* help without leaving. With VimTutor you *practise* without leaving. Same lesson as the shell sessions — you do not have to bounce out to a browser to get good at the tools that are already in front of you.

**Why this is useful:** configs on servers, quick edits in `/etc`, scratch notes in `/tmp` — if you can open, change, save, and quit in Vim, you can fix things anywhere Linux is installed. Nano is fine; Vim being “always there” is what makes it a solid default skill.

## What I can run here

On this machine (WSL):

```bash
command -v vim
# /usr/bin/vim — VIM 9.1
command -v vimtutor
# /usr/bin/vimtutor
command -v nano
# /usr/bin/nano
```

Practise loop (same as the course order — basics first):

```bash
vim /tmp/nyaks-vim-note.txt
# i  → type a line
# Esc → :wq
cat /tmp/nyaks-vim-note.txt
vimtutor   # when you want the interactive path
```

---

*RH024 learning note — Editing files with Vim.*
