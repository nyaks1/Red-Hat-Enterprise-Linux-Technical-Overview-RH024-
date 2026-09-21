# Linux distributions

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** Linux Distributions Unveiled (Ricardo Da Costa)  
**Logged:** 2026-09-21  
**Why this note exists:** public learning trail for the Red Hat track. Skill first; the paid programme and Atos internship are upside, not the reason I study.

## What a distribution actually is

A Linux distribution (distro) is a complete operating system built around the Linux kernel. The kernel is the shared foundation — the central core every Linux system relies on. What separates distros is everything wrapped around that kernel: tools, applications, system defaults, package management, release cadence, and support model.

Same heart. Different bodies. That is why "Linux" is a family of products, not a single product.

## The Red Hat family: upstream to production

These distros share the Red Hat lineage, but they are not interchangeable.

| Distro | Role | Who it is for |
| --- | --- | --- |
| **Fedora** | Upstream project — cutting-edge features, experiments, latest updates | People who want the playground and accept risk |
| **CentOS Stream** | Midstream rolling preview of the next RHEL minor release | Developers and partners who want to see and influence what is coming |
| **RHEL** | Polished, enterprise-grade product | Production systems where stability, security, and support are mission-critical |

Innovation does not teleport into production. New work lands in Fedora, is previewed through CentOS Stream, then is hardened into RHEL after testing and QA. Red Hat's design bet is balance: innovate without sacrificing reliability.

## Package managers shape your whole software experience

- **RHEL, CentOS Stream, Fedora:** RPM package manager (a veteran; RPM dates back to 1997). Install, update, remove — `rpm` / `dnf` territory.
- **Debian / Ubuntu:** APT and dpkg.

RPM packages are not compatible with APT packages and vice versa. The distro also decides what ships out of the box (Python, Node.js, GCC, Java, and so on). Your package manager is not a footnote — it shapes almost every day you spend on the machine.

## Predictability and support (why enterprises pay)

- New major RHEL versions roughly every **three years**
- Upgrade tooling (Leap) exists to make major jumps smoother
- Support runs in phases:
  1. **Full support** — about the first five years: features, bug fixes, security updates
  2. **Maintenance support** — the next stretch: mainly security patches
  3. **Extended update support** — optional add-on for selected security patches after the first two phases

Other distros optimise differently. Red Hat optimises for planning and the long haul.

## The part I liked most: open source means it can be mine

This is the section I actually care about, so I am writing it in plain words.

Almost everything in a Linux distribution is open source. That is not only "free as in price." It means:

1. **I can look at the code** — the system is not a black box.
2. **I can change it** — tweak behaviour to fit how *I* work.
3. **I can share the improvement** — if my change helps others, it can re-enter the ecosystem.

No costly or restrictive licence sitting between me and the system I run.

Red Hat does not only consume open source; it contributes back. Innovations such as **systemd**, **KVM**, and **Tuned** started in this world and now power many other distributions too. The ecosystem is vibrant because borrowing, learning, and building on each other's work are normal — a two-way street.

There is also a practical door for students and independents: Red Hat's **no-cost developer subscription** for individuals (non-production use, up to 16 systems, updates plus self-service support). I do not need a company budget to learn on real RHEL.

**Why this hits for me:** closed systems train you to stay a user. Open systems train you to become an operator — someone who can inspect, repair, and own the stack. That is the skill the Red Hat track is actually selling.

*Build the man.* Every time I read a config, change a default, rebuild something, or fix a service in the open, the OS becomes less "theirs" and more mine. Ownership is a habit, not a vibe.

## Flexibility and standards

- Want a full desktop? GNOME is available.
- Prefer headless servers and the command line? Also valid.
- Red Hat follows the **File Hierarchy Standard (FHS)**: paths like `/etc`, `/usr`, and `/var` sit where you expect. Not every distro sticks to standards 100%; Red Hat does it for predictability and easier troubleshooting.

Shared tools and kernels do not mean identical day-to-day experience. Defaults, configuration, and release schedule change how the machine feels — like two cars built from similar parts but tuned very differently.

## Hands-on checklist

- [x] Red Hat Developer account (2026-09-21) — Sandbox ≠ RHEL subscription
- [x] Download RHEL 9.8 Boot ISO (2026-09-21)
- [x] Touch RHEL 9.8 userspace without a hypervisor (UBI container, 2026-09-21)
- [ ] Confirm no-cost RHEL developer subscription
- [ ] Boot the ISO in a VM and prove `subscription-manager list --consumed`

## Evidence log (proof of work)

| Date | What | Result |
| --- | --- | --- |
| 2026-09-21 | Downloaded `rhel-9.8-x86_64-boot.iso` | 1,440 MB on disk; not a partial `.crdownload` |
| 2026-09-21 | Mounted ISO on Windows | Drive `D:`, label `RHEL-9-8-0-BaseO`, contents `EFI/`, `images/`, `isolinux/` |
| 2026-09-21 | Ran Red Hat UBI9 in Docker (WSL Ubuntu 24.04) | `os-release` reports **Red Hat Enterprise Linux 9.8 (Plow)** |
| 2026-09-21 | Hands-on in UBI container | `rpm -q rpm` → `rpm-4.16.1.3-40.el9.x86_64`; `/etc`, `/usr`, `/var` present |
| 2026-09-21 | `dnf repolist` in UBI | UBI repos listed (`ubi-9-baseos-rpms`, `ubi-9-appstream-rpms`, `ubi-9-codeready-builder-rpms`); **not registered** — `Unable to read consumer identity` |

How to re-run (PowerShell → WSL):

```powershell
wsl -d Ubuntu -- docker run --rm -it registry.access.redhat.com/ubi9/ubi:latest bash
```

```bash
cat /etc/os-release
rpm -q rpm
ls -ld /etc /usr /var
dnf repolist
exit
```

**Honest boundary:** UBI is free RHEL *userspace* for containers. `dnf repolist` showed the entitlement wall — this system is not registered with an entitlement server. UBI is not a subscribed RHEL install. Subscription and VM boxes stay open.

No VirtualBox/VMware on this machine at time of proof. ISO is ready on disk for the VM step when a hypervisor exists.

## Standing gates for this track

- **Brand fit:** Linux/RHEL is foundation work for Cybersecurity and FinTech infrastructure. Hours here count.
- **Shovel, not gold:** learn the platform others build on. Platform skill compounds; one-off app ideas do not.
- **POPIA:** this repo is public learning notes only. No personal data, no client data, no credentials. If I later demo anything that touches people data, state what is collected, where it is hosted, and how it is deleted — before the demo, not after.

---

*Learning note for RH024. Based on the course session. Transcript slips corrected for the written record: "System B" → **systemd**; "Center Stream" → **CentOS Stream**; path names like "Etsy / USR / bar" → **`/etc` / `/usr` / `/var`**.*
