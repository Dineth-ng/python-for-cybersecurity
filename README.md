# Python for Cybersecurity — Learning Journey

> A hands-on, beginner-friendly roadmap for learning Python through real cybersecurity workflows.
> Built in public — anyone can clone this repo and follow the same path.

![Progress](https://img.shields.io/badge/Phase-1%20of%204-blue)
![Language](https://img.shields.io/badge/Language-Python%203.10+-green)
![Focus](https://img.shields.io/badge/Focus-Cybersecurity-red)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

---

## About This Repo

This is my personal learning journey — documenting everything I learn about Python as it applies to cybersecurity.

I built this repo so others can follow the exact same roadmap. Every script is written from scratch as I learn, with comments explaining what each line does and why it matters in a security context.

If you are also learning Python for cybersecurity, feel free to:
- **Star** this repo to follow along
- **Fork** it and track your own progress
- **Open an issue** if you spot a mistake or want to suggest something

---

## Roadmap Overview

| Phase | Topic | Duration | Status |
|-------|-------|----------|--------|
| 1 | Python Foundations | Weeks 1–3 | 🔄 In progress |
| 2 | Log Parsing & IOC Handling | Weeks 4–6 | ⏳ Not started |
| 3 | Networking & Automation | Weeks 7–10 | ⏳ Not started |
| 4 | Portfolio Project | Weeks 11–14 | ⏳ Not started |

<img width="512" height="682" alt="image" src="https://github.com/user-attachments/assets/abec792a-c6c4-42fe-b72e-843547b78a50" />


---

## Phase 1 — Python Foundations (Weeks 1–3)

Learn the core Python building blocks needed before writing any security tools.

**What you will learn:**
- Variables, data types, lists, and dictionaries
- Loops (`for`, `while`) and conditions (`if`, `elif`, `else`)
- Reading and writing files
- Writing reusable functions
- Handling errors with `try` / `except`
- Regex patterns with the `re` module

**Mini project:** A word counter script that reads any `.txt` file and outputs line count, word count, and unique words — the foundation of log reading.

📁 [`phase-1-foundations/`](./phase-1-foundations/)

---

## Phase 2 — Log Parsing & IOC Handling (Weeks 4–6)

Learn how SOC analysts use Python to turn raw logs into useful timelines and extract threat indicators.

**What you will learn:**
- Parsing CSV, JSON, and raw text log files
- Extracting IOCs: IP addresses, domains, file hashes
- Matching IOC lists against log data
- Hashing files with `hashlib` (MD5, SHA256)
- Building a clean event timeline from messy log data

**Mini project:** A log triage tool that reads an `auth.log` file, flags failed login attempts, and outputs a clean report.

📁 [`phase-2-log-parsing/`](./phase-2-log-parsing/)

---

## Phase 3 — Networking & Automation (Weeks 7–10)

Build your first real security tools using Python's networking libraries.

**What you will learn:**
- TCP/UDP connections with the `socket` module
- HTTP requests with the `requests` library
- Building a simple port scanner
- Running system commands with `subprocess`
- Building CLI tools with `argparse`
- Enriching IPs using free threat intel APIs (VirusTotal, AbuseIPDB)

**Mini project:** A port scanner + IP enrichment tool that scans a target and checks IPs against threat intelligence feeds.

📁 [`phase-3-networking/`](./phase-3-networking/)

---

## Phase 4 — Portfolio Project (Weeks 11–14)

Build one complete, well-documented cybersecurity tool to publish on GitHub and mention in a CV.

**Project: SOC Alert Triage Tool**

A command-line tool that:
- Reads alert log files (CSV or JSON)
- Extracts and deduplicates IOCs
- Enriches IPs and domains via API
- Outputs a formatted investigation report

📁 [`phase-4-portfolio-project/`](./phase-4-portfolio-project/)

---

## How to Use This Repo

### Prerequisites
- Python 3.10 or higher installed
- A text editor (VS Code recommended)
- Basic command line knowledge

### Getting started

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/python-for-cybersecurity.git
cd python-for-cybersecurity

# Install dependencies
pip install -r requirements.txt

# Run any script
python phase-1-foundations/01_variables_and_types.py
```

### Folder structure

```
python-for-cybersecurity/
│
├── README.md                         ← You are here
├── PROGRESS.md                       ← Weekly learning log
├── requirements.txt                  ← Python packages used
│
├── phase-1-foundations/
│   ├── README.md
│   ├── 01_variables_and_types.py
│   ├── 02_loops_and_conditions.py
│   ├── 03_file_io.py
│   ├── 04_functions.py
│   ├── 05_error_handling.py
│   ├── 06_regex_basics.py
│   └── mini_project_word_counter.py
│
├── phase-2-log-parsing/
│   ├── README.md
│   ├── 01_parse_csv_logs.py
│   ├── 02_extract_iocs.py
│   ├── 03_ioc_matching.py
│   ├── 04_file_hashing.py
│   ├── 05_build_timeline.py
│   ├── mini_project_log_triage.py
│   └── sample_logs/
│       ├── auth.log
│       └── access.log
│
├── phase-3-networking/
│   ├── README.md
│   ├── 01_socket_basics.py
│   ├── 02_http_requests.py
│   ├── 03_port_scanner.py
│   ├── 04_subprocess_commands.py
│   ├── 05_api_enrichment.py
│   └── mini_project_ip_scanner.py
│
└── phase-4-portfolio-project/
    ├── README.md
    ├── main.py
    ├── parser.py
    ├── enricher.py
    └── reporter.py
```

---

## Resources I Am Using

| Resource | Type | Link |
|----------|------|-------|
| TryHackMe Python Basics | Interactive lab | [tryhackme.com](https://tryhackme.com/room/pythonbasics) |
| TryHackMe SOC Level 1 | Learning path | [tryhackme.com](https://tryhackme.com/path/outline/soclevel1) |
| Automate the Boring Stuff | Free book | [automatetheboringstuff.com](https://automatetheboringstuff.com) |
| Black Hat Python | Book | Available on Amazon |
| Baeldung | Spring/backend articles | [baeldung.com](https://baeldung.com) |

---

## Progress Tracking

I log my weekly progress in [`PROGRESS.md`](./PROGRESS.md). This includes what I learned, what was hard, and what I built each week.

---

## Topics Covered So Far

- [ ] Variables and data types
- [ ] Loops and conditionals
- [ ] File I/O
- [ ] Functions
- [ ] Error handling
- [ ] Regex
- [ ] Log parsing
- [ ] IOC extraction
- [ ] File hashing
- [ ] IOC matching
- [ ] Socket programming
- [ ] HTTP requests
- [ ] Port scanning
- [ ] API enrichment
- [ ] Portfolio project

---

## Disclaimer

All scripts in this repo are written for **educational purposes only**. Never run scanning or network tools against systems you do not own or have explicit permission to test.

---

## Connect

If you are following this roadmap, I'd love to know! Open an issue, leave a comment, or connect with me on LinkedIn.

*Happy learning — one script at a time.*
