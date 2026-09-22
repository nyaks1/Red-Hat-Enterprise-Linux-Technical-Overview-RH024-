# Insights Image Builder

**Course:** RH024 — Red Hat Enterprise Linux Technical Overview  
**Session:** Insights Image Builder / Image Builder Essentials (Ricardo Da Costa)  
**Logged:** 2026-09-22

## What the course covered

A **golden image** is a clean, consistent template — a ready snapshot of an OS (plus what you put in it) that you stamp out for servers or VMs in a data centre, cloud, or at the edge. Deployments stay rapid and predictable; less guesswork.

Red Hat ships **two** image builders (both tied to a RHEL subscription):

| Tool | Where | Best for |
| --- | --- | --- |
| **Insights Image Builder** | Hosted — **web UI** in the Red Hat Hybrid Cloud Console (Inventory → Images) | No build infra to maintain; simple cloud workflow |
| **RHEL Image Builder** | Installed on-prem (CLI + optional web UI in RHEL web console) | More control / air-gapped or local build hosts |

Default is a **minimal** install. Then you add **only** what you need: packages, custom scripts, security/compliance profiles. Same idea works for physical, VMs, public cloud, and edge.

### The part I loved: the blueprint

You define an **image blueprint** — architecture, packages, users, firewall ports, systemd units — and the builder produces that image. You are not stuck with a kitchen-sink template full of apps you will never use.

Course demo choices (RHEL 10, x86_64):

- Output: general virtualization guest (**qcow2**)  
- Registration: auto / activation key / **register later**  
- OpenSCAP compliance profiles: optional  
- Partitioning: recommended  
- Extra packages: e.g. **OpenJDK**  
- Users, timezone (UTC), DNS, hostname  
- Firewall: port **8080**  
- systemd services to enable  

Then **Create blueprint** → **Build image** → download the qcow2 for VMs.

## Where to click (this one is the web, not the terminal)

1. Browser → **[https://console.redhat.com](https://console.redhat.com)**  
2. Sign in with your Red Hat account  
3. Under **Red Hat Enterprise Linux** → **Insights** / hybrid cloud console  
4. Open **Inventory** → **Images** (Image Builder)  
5. **Create image blueprint** → RHEL 10, x86_64, packages, firewall, etc.

Deep-link (same console, image builder area):

- [https://console.redhat.com/insights/image-builder](https://console.redhat.com/insights/image-builder)

If the UI path moves, search in the console for **Image Builder**. Docs: Red Hat Enterprise Linux → *creating customized RHEL images* / Image Builder on access.redhat.com.

## What I enjoyed

I love the **blueprint** model: build the image that fits **my** needs so I am not stuck with applications I will never use. That is the opposite of “install everything and uninstall forever.”

This session is **web**, not terminal — same idea as `man` vs the browser earlier: sometimes the UI is the right tool. Insights Image Builder means **no extra build infrastructure**; the catalogue of choices (packages, compliance, ports, services) is the shovel for consistent machines.

**Why this is useful:** golden images beat snowflake VMs. One blueprint → many identical starts → fewer “works on my box” surprises.

## Screenshots (you capture in the console)

Browser session on console.redhat.com — drop images into `evidence/` when you have them (keep account email out of frame if you can):

| Suggested shot | File name to use |
| --- | --- |
| Console → Image Builder landing | `evidence/2026-09-22-image-builder-console.png` |
| Create blueprint form (packages / firewall) | `evidence/2026-09-22-image-builder-blueprint-form.png` |
| Blueprint created / build queue | `evidence/2026-09-22-image-builder-build.png` |

*(Screenshots pending — this flow is on the web; terminal capture does not apply here.)*

---

*RH024 learning note — Insights Image Builder.*
