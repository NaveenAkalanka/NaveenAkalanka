<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/hero-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/hero-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/hero-mobile.svg">
  <img src="./Assets/operations/hero.svg" width="100%" alt="Naveen Akalanka. An operations log: from networking to resilient systems.">
</picture>

<p align="center">
  <a href="#operator"><img src="./Assets/operations/button-story.svg" width="172" alt="01 — Open the story"></a>
  <a href="#projects"><img src="./Assets/operations/button-projects.svg" width="172" alt="02 — Inspect the projects"></a>
  <a href="#lab"><img src="./Assets/operations/button-lab.svg" width="172" alt="03 — Trace the lab"></a>
  <a href="#activity"><img src="./Assets/operations/button-activity.svg" width="172" alt="04 — Read the activity"></a>
</p>

<p align="center"><b>Infrastructure engineer · Sri Lanka · Linux & networking · Cloud & DevOps</b><br>
A story told through systems, experiments, and the tools I build.</p>

## Operator

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/chapter-01-still.svg">
  <img src="./Assets/operations/chapter-01.svg" width="100%" alt="Chapter 01 — The operator">
</picture>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/identity-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/identity-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/identity-mobile.svg">
  <img src="./Assets/operations/identity.svg" width="100%" alt="Animated terminal: Naveen Akalanka, infrastructure engineer; networking roots, cloud and automation direction.">
</picture>

<details>
<summary><kbd>OPEN</kbd> <b>The story behind the prompt</b></summary>

I started in networking and kept going deeper into Linux, virtualization, and self-hosted systems. My focus is on **cloud, DevOps, infrastructure as code, and automation**, grounded in understanding how the underlying systems work.

I use my Proxmox lab to test ideas, troubleshoot failures, and document what I learn. When existing tools don’t solve a problem, I build one. My background in graphic and 3D design shapes how those tools communicate.

</details>

## Projects

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/chapter-02-still.svg">
  <img src="./Assets/operations/chapter-02.svg" width="100%" alt="Chapter 02 — Six case studies, one engineering mindset">
</picture>

These are the steps in my engineering story: **discover → observe → understand → package → protect → operate**. The first five are public software projects; the sixth is my infrastructure lab.

### 01 / Discover the network

<a href="https://github.com/NaveenAkalanka/ScanEye">
<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/project-scaneye-still.svg">
  <img src="./Assets/operations/project-scaneye.svg" width="100%" alt="ScanEye — new amber and green project artwork">
</picture>
</a>

A browser can’t scan your local network. I built the bridge: **Nmap discovery inside Docker**, with results streamed to a React dashboard over WebSockets.

<sub>Docker · Nmap · Node.js · React · WebSockets</sub>

<details>
<summary><kbd>INSPECT</kbd> <b>The engineering idea</b></summary>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-scaneye-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-scaneye-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/case-scaneye-mobile.svg">
  <img src="./Assets/operations/case-scaneye.svg" width="100%" alt="Animated ScanEye case-study terminal: architecture, problem, and approach.">
</picture>

A browser stays inside its security boundary. The backend performs the network discovery and sends results to the interface. This separation is the core architectural decision.

</details>

<a href="https://github.com/NaveenAkalanka/ScanEye"><img src="./Assets/operations/button-source.svg" width="174" alt="Open ScanEye repository"></a>

### 02 / See the system

<a href="https://github.com/NaveenAkalanka/ClusterEye">
<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/project-clustereye-still.svg">
  <img src="./Assets/operations/project-clustereye.svg" width="100%" alt="ClusterEye — new amber and green project artwork">
</picture>
</a>

Monitoring becomes useful when it gives you a view across the system. **ClusterEye brings cluster monitoring and management into one dashboard**, and helped shape the architecture I later explored in ScanEye.

<sub>JavaScript · Node.js · Docker</sub>

<details>
<summary><kbd>INSPECT</kbd> <b>What this project taught me</b></summary>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-clustereye-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-clustereye-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/case-clustereye-mobile.svg">
  <img src="./Assets/operations/case-clustereye.svg" width="100%" alt="Animated ClusterEye case-study terminal: architecture, problem, and approach.">
</picture>

Visibility is a systems problem as much as a UI problem. ClusterEye was an earlier step in exploring how an interface communicates with the infrastructure it represents.

</details>

<a href="https://github.com/NaveenAkalanka/ClusterEye"><img src="./Assets/operations/button-source.svg" width="174" alt="Open ClusterEye repository"></a>

### 03 / Understand the foundation

<a href="https://github.com/NaveenAkalanka/NuxView">
<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/project-nuxview-still.svg">
  <img src="./Assets/operations/project-nuxview.svg" width="100%" alt="NuxView — new amber and green project artwork">
</picture>
</a>

Services sit on top of filesystems. **NuxView turns Linux directory structure into something you can explore visually**, making the layers underneath an application easier to understand.

<sub>Linux · TypeScript · Node.js · React</sub>

<details>
<summary><kbd>INSPECT</kbd> <b>Why it belongs in my toolkit</b></summary>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-nuxview-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-nuxview-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/case-nuxview-mobile.svg">
  <img src="./Assets/operations/case-nuxview.svg" width="100%" alt="Animated NuxView case-study terminal: architecture, problem, and approach.">
</picture>

Knowing what runs underneath a service starts with understanding its environment. NuxView scans local directories and exposes their structure through a web interface.

</details>

<a href="https://github.com/NaveenAkalanka/NuxView"><img src="./Assets/operations/button-source.svg" width="174" alt="Open NuxView repository"></a>

### 04 / Package a useful service

<a href="https://github.com/NaveenAkalanka/Savit">
<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/project-savit-still.svg">
  <img src="./Assets/operations/project-savit.svg" width="100%" alt="Savit — new amber and green project artwork">
</picture>
</a>

A self-hosted home for saved links—with list, grid, and 3D constellation views. **Savit connects application design with containerized delivery**, explicit configuration, and a persistent database.

<sub>Docker · TypeScript · React · Fastify · libSQL/Turso</sub>

<details>
<summary><kbd>INSPECT</kbd> <b>Inspect the deployment story</b></summary>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-savit-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-savit-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/case-savit-mobile.svg">
  <img src="./Assets/operations/case-savit.svg" width="100%" alt="Animated Savit case-study terminal: architecture, problem, and approach.">
</picture>

A multi-stage Docker build packages the application. The container is stateless; saved data lives in libSQL/Turso. Database configuration is explicit, and TLS belongs at the reverse proxy. The 3D view uses three.js.

</details>

<a href="https://github.com/NaveenAkalanka/Savit"><img src="./Assets/operations/button-source.svg" width="174" alt="Open Savit repository"></a>

### 05 / Respect the workspace

<a href="https://github.com/NaveenAkalanka/lookmd">
<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/project-lookmd-still.svg">
  <img src="./Assets/operations/project-lookmd.svg" width="100%" alt="lookmd — new amber and green project artwork">
</picture>
</a>

A self-hosted Markdown reader and editor that treats a folder as a workspace. **lookmd combines a scoped filesystem API with a single-container deployment** and explicit, conflict-aware saves.

<sub>Docker · TypeScript · Fastify · React · CodeMirror</sub>

<details>
<summary><kbd>INSPECT</kbd> <b>Inspect the engineering boundaries</b></summary>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-lookmd-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-lookmd-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/case-lookmd-mobile.svg">
  <img src="./Assets/operations/case-lookmd.svg" width="100%" alt="Animated lookmd case-study terminal: architecture, problem, and approach.">
</picture>

The backend scopes file access to a workspace. Writes are explicit and hash-checked to detect changes on disk. A Docker image serves the client and API together, with the document folder mounted as data.

</details>

<a href="https://github.com/NaveenAkalanka/lookmd"><img src="./Assets/operations/button-source.svg" width="174" alt="Open lookmd repository"></a>

### 06 / Put the layers together

<a href="#lab">
<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/project-homelab-still.svg">
  <img src="./Assets/operations/project-homelab.svg" width="100%" alt="Proxmox Lab — new amber and green project artwork">
</picture>
</a>

My high-availability **Proxmox home lab** is where networking, Linux, virtual machines, containers, and automation meet. It is a working environment for experiments and troubleshooting.

<sub>Proxmox · Linux · VMs · LXC · Networking</sub>

<details>
<summary><kbd>INSPECT</kbd> <b>Open the lab case study</b></summary>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-homelab-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/case-homelab-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/case-homelab-mobile.svg">
  <img src="./Assets/operations/case-homelab.svg" width="100%" alt="Animated Proxmox Lab case-study terminal: architecture, problem, and approach.">
</picture>

This is my existing home-lab practice, not a separate software release. I use it to design, break, and harden systems, then carry those lessons into cloud and automation work.

</details>

<a href="#lab"><img src="./Assets/operations/button-lab.svg" width="174" alt="Explore the lab"></a>

<details>
<summary><kbd>ARCHIVE</kbd> <b>Other experiments</b></summary>

[PoseFit V2](https://github.com/NaveenAkalanka/PoseFit-V2) · [ScrollSync](https://github.com/NaveenAkalanka/ScrollSync) · [SerenityEcho](https://github.com/NaveenAkalanka/SerenityEcho) · [DesignFlow](https://github.com/NaveenAkalanka/DesignFlow) · [MFTrack](https://github.com/NaveenAkalanka/MFTrack) · [KokoMate](https://github.com/NaveenAkalanka/KokoMate) · [DailyBurn](https://github.com/NaveenAkalanka/DailyBurn) · [PoseFit](https://github.com/NaveenAkalanka/PoseFit)

</details>

## Lab

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/chapter-03-still.svg">
  <img src="./Assets/operations/chapter-03.svg" width="100%" alt="Chapter 03 — Design, deploy, observe, improve">
</picture>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/pipeline-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/pipeline-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/pipeline-mobile.svg">
  <img src="./Assets/operations/pipeline.svg" width="100%" alt="Animated infrastructure workflow: understand the foundation, package services, automate repeatable work, observe and improve.">
</picture>

<details open>
<summary><kbd>RUNBOOK</kbd> <b>Follow the delivery plan</b></summary>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/deployment-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/deployment-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/deployment-mobile.svg">
  <img src="./Assets/operations/deployment.svg" width="100%" alt="Animated delivery-plan terminal: understand dependencies, build containers, configure, validate, observe, improve.">
</picture>

</details>

<details>
<summary><kbd>TOOLCHAIN</kbd> <b>Explore my infrastructure and cloud toolkit</b></summary>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/skills-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/skills-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/skills-mobile.svg">
  <img src="./Assets/operations/skills.svg" width="100%" alt="Linux, Proxmox, LXC, TrueNAS, ZFS, Cisco, DNS, DHCP, VLANs, Nmap, Docker, Kubernetes, Ansible, GitHub Actions, Azure, AWS, TypeScript, Python, Node.js and React.">
</picture>

Also in the mix: **Minikube · Cloudflare · Traefik · n8n · Wireshark**.

These are tools I work with and areas I’m developing—not proficiency scores or claims of production-scale deployments.

</details>

## Activity

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/chapter-04-still.svg">
  <img src="./Assets/operations/chapter-04.svg" width="100%" alt="Chapter 04 — Real public data, a continuing story">
</picture>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/NaveenAkalanka/NaveenAkalanka/output/activity-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="https://raw.githubusercontent.com/NaveenAkalanka/NaveenAkalanka/output/activity-still.svg">
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/NaveenAkalanka/NaveenAkalanka/output/activity-mobile.svg">
  <img src="https://raw.githubusercontent.com/NaveenAkalanka/NaveenAkalanka/output/activity.svg" width="100%" alt="Public GitHub activity: owned repositories, repository stars, followers, recent public events, repository languages and recent project pushes.">
</picture>

<sub>Refreshed every 12 hours by this repository. The chart shows sampled public events—not total commits—and includes its last successful update time.</sub>

<details>
<summary><kbd>PLAY</kbd> <b>Follow the contribution trail</b></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NaveenAkalanka/NaveenAkalanka/output/github-contribution-grid-snake-dark.svg">
  <img src="https://raw.githubusercontent.com/NaveenAkalanka/NaveenAkalanka/output/github-contribution-grid-snake.svg" width="100%" alt="Amber snake moving through my GitHub contribution history.">
</picture>

</details>

## Next chapter

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/chapter-05-still.svg">
  <img src="./Assets/operations/chapter-05.svg" width="100%" alt="Chapter 05 — Learning, cloud and automation">
</picture>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./Assets/operations/journey-mobile-still.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./Assets/operations/journey-still.svg">
  <source media="(max-width: 600px)" srcset="./Assets/operations/journey-mobile.svg">
  <img src="./Assets/operations/journey.svg" width="100%" alt="Career route: HND with Distinction, first-class BSc, academic and research awards, and a continuing focus on cloud and automation.">
</picture>

<details>
<summary><kbd>RECORD</kbd> <b>Education & recognition</b></summary>

**BSc (Hons) Computer Networks** · University of Wolverhampton<br>
First Class Honours · 2024

**Highest Academic Achievement (Batch Top)** and **Best Dissertation / Research Project** awards · October 2025

**HND Computing — Networking & Telecommunications** · Pearson<br>
Distinction · 2021–2023

</details>

My next chapter builds on that foundation: **cloud infrastructure, repeatable delivery, and automation that solves real operational problems**. I use AI agents to accelerate exploration and implementation while owning the architecture, review, and validation.

<p align="center">
  <b>Have a system worth understanding or a problem worth solving?</b><br><br>
  <a href="https://www.linkedin.com/in/naveen-akalanka"><img src="./Assets/operations/button-contact.svg" width="224" alt="Connect with Naveen Akalanka on LinkedIn"></a>
</p>

<p align="center"><sub>naveen@lab:~$ <b>keep_building</b> ▋</sub></p>
