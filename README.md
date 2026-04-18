# Python Port Scanner

A fast, multithreaded TCP port scanner built in Python using sockets and concurrent execution.
This tool allows scanning of common or custom port ranges on a target host and identifies basic services running on open ports.

---

## Features

* Multithreaded TCP port scanning (faster than sequential scanning)
* Supports both IP addresses and domain names
* Custom port ranges or predefined common ports
* Basic service detection for well-known ports
* Command-line interface using argparse
* Clean and readable output with scan timing

---

## How It Works

The scanner attempts to establish a TCP connection to each specified port using Python's socket module.
If the connection succeeds, the port is marked as open.
Concurrency is implemented using ThreadPoolExecutor to improve performance.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/port-scanner.git
cd port-scanner
```

No external dependencies are required. The script uses only Python standard libraries.

---

## Usage

Basic scan:

```bash
python portscanner.py google.com
```

Scan specific ports:

```bash
python portscanner.py google.com -p 80,443
```

Scan a range of ports:

```bash
python portscanner.py google.com -p 1-1000
```

Adjust number of threads:

```bash
python portscanner.py google.com -p 1-1000 -t 100
```

---

## Example Output

```
Scanning google.com [142.250.x.x] with 50 threads...

[+] 80    OPEN  HTTP
[+] 443   OPEN  HTTPS

Scan Results
------------------------------
Open ports: [80, 443]
Scan completed in 0.84 seconds
```

---

## Project Structure

```
port-scanner/
│
├── portscanner.py
├── README.md
└── .gitignore
```

---

## Disclaimer

This tool is intended for educational purposes only.
Only scan systems you own or have explicit permission to test.

---

## What This Project Demonstrates

* Understanding of TCP/IP networking fundamentals
* Practical use of Python socket programming
* Implementation of concurrency for performance optimization
* Design of command-line tools using argparse

---

## Future Improvements

* To Be Determined
---
