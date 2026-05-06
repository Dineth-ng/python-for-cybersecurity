# Progress Log

This file tracks my week-by-week learning progress through the Python for Cybersecurity roadmap.

Updated every week. Honest notes — including what was confusing, not just what went well.

---

## How to Read This

Each week has:
- **What I studied** — topics and scripts I worked on
- **What I built** — any script or mini project completed
- **What was hard** — honest notes on where I got stuck
- **Time spent** — approximate hours that week
- **Resources used** — links or books referenced

---

## Phase 1 — Python Foundations

### Week 1

**What I studied:**
- Variables, strings, integers, lists, dictionaries
- Basic print statements and input/output
- How Python handles different data types

**What I built:**
- `01_variables_and_types.py` — experimenting with different variable types and printing them

**What was hard:**
- Understanding the difference between a list and a dictionary and when to use each

**Time spent:** — hours

**Resources used:**
- Automate the Boring Stuff — Chapter 1 and 2
- TryHackMe Python Basics room

---

### Week 2

**What I studied:**
- `for` loops and `while` loops
- `if`, `elif`, `else` conditions
- Combining loops with conditions to filter data

**What I built:**
- `02_loops_and_conditions.py`
- `03_file_io.py` — reading a text file line by line

**What was hard:**
- Loop indentation errors — Python is strict about spacing
- Understanding when to use `while` vs `for`

**Time spent:** — hours

**Resources used:**
- Automate the Boring Stuff — Chapter 2 and 3

---

### Week 3

**What I studied:**
- Writing and calling functions with `def`
- Return values and function arguments
- `try` / `except` for error handling
- Introduction to regex with the `re` module

**What I built:**
- `04_functions.py`
- `05_error_handling.py`
- `06_regex_basics.py` — extracting IP addresses from a string using regex
- `mini_project_word_counter.py` — reads any `.txt` file and counts lines, words, unique words

**What was hard:**
- Regex syntax is confusing at first — `\d+`, `\b`, groups
- Understanding why functions need `return` not just `print`

**Time spent:** — hours

**Resources used:**
- Python `re` module documentation
- regex101.com — for testing patterns

---

## Phase 2 — Log Parsing & IOC Handling

### Week 4

**What I studied:**
- Reading CSV files with the `csv` module
- Reading JSON files with the `json` module
- Parsing raw log text with string methods and regex

**What I built:**
- `01_parse_csv_logs.py`

**What was hard:**
- 

**Time spent:** — hours

**Resources used:**
- 

---

### Week 5

**What I studied:**
- Extracting IP addresses, domains, and file hashes from unstructured text
- Deduplicating extracted indicators using sets
- File hashing with `hashlib` (MD5 and SHA256)

**What I built:**
- `02_extract_iocs.py`
- `04_file_hashing.py`

**What was hard:**
- 

**Time spent:** — hours

**Resources used:**
- 

---

### Week 6

**What I studied:**
- Comparing IOC lists against log data
- Sorting events by timestamp to build a timeline
- Formatting and writing output reports to a file

**What I built:**
- `03_ioc_matching.py`
- `05_build_timeline.py`
- `mini_project_log_triage.py` — full log triage tool that reads `auth.log`, flags failed logins, outputs a report

**What was hard:**
- 

**Time spent:** — hours

**Resources used:**
- 

---

## Phase 3 — Networking & Automation

### Week 7

**What I studied:**
- How TCP and UDP connections work
- Python `socket` module basics — connecting to a host and port

**What I built:**
- `01_socket_basics.py`

**What was hard:**
- 

**Time spent:** — hours

**Resources used:**
- 

---

### Week 8

**What I studied:**
- HTTP requests with the `requests` library
- GET and POST requests, reading response status codes and headers

**What I built:**
- `02_http_requests.py`

**What was hard:**
- 

**Time spent:** — hours

**Resources used:**
- 

---

### Week 9

**What I studied:**
- Building a basic port scanner with `socket` and `threading`
- Running system commands with `subprocess`
- Building CLI tools with `argparse`

**What I built:**
- `03_port_scanner.py`
- `04_subprocess_commands.py`

**What was hard:**
- 

**Time spent:** — hours

**Resources used:**
- 

---

### Week 10

**What I studied:**
- Calling threat intelligence APIs (VirusTotal, AbuseIPDB)
- Parsing API JSON responses
- Enriching a list of IPs automatically

**What I built:**
- `05_api_enrichment.py`
- `mini_project_ip_scanner.py` — scans ports and enriches IPs via threat intel API

**What was hard:**
- 

**Time spent:** — hours

**Resources used:**
- VirusTotal public API docs
- AbuseIPDB API docs

---

## Phase 4 — Portfolio Project

### Week 11

**What I studied / planned:**
- Designed the structure of the SOC alert triage tool
- Planned input format, output format, and modules

**What I built:**
- Skeleton files: `main.py`, `parser.py`, `enricher.py`, `reporter.py`

**What was hard:**
- 

**Time spent:** — hours

**Resources used:**
- 

---

### Week 12

**What I built:**
- `parser.py` — reads and cleans alert log input
- `enricher.py` — calls threat intel API for each IOC

**What was hard:**
- 

**Time spent:** — hours

---

### Week 13

**What I built:**
- `reporter.py` — formats and writes investigation report
- `main.py` — ties all modules together with CLI arguments

**What was hard:**
- 

**Time spent:** — hours

---

### Week 14

**What I did:**
- Wrote the phase 4 `README.md` with full usage instructions
- Tested the complete tool end to end with sample logs
- Cleaned up comments throughout all scripts
- Updated the main `README.md` checklist

**Total project status:** Complete

**Time spent:** — hours

---

## Overall Stats

| Phase | Status | Total hours |
|-------|--------|-------------|
| Phase 1 — Foundations | 🔄 In progress | — |
| Phase 2 — Log parsing | ⏳ Not started | — |
| Phase 3 — Networking | ⏳ Not started | — |
| Phase 4 — Portfolio project | ⏳ Not started | — |
| **Total** | | **—** |

---

## Reflections

*(Add personal notes here at the end of each phase — what clicked, what surprised you, what you would tell your past self)*

### After Phase 1
*Coming soon*

### After Phase 2
*Coming soon*

### After Phase 3
*Coming soon*

### After Phase 4
*Coming soon*

---

*Last updated: May 2026*
