import socket
import argparse
import concurrent.futures
import time
from functools import partial

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3389: "RDP"
}

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                service = COMMON_PORTS.get(port, "Unknown")
                return (port, service)
    except socket.error:
        return None
    return None


def scan_host(target, ports, threads):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid hostname or IP")
        return

    print(f"\nScanning {target} [{ip}] with {threads} threads...\n")

    start_time = time.time()
    open_ports = []

    scan = partial(scan_port, ip)

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(scan, ports)

    for result in results:
        if result:
            port, service = result
            print(f"[+] {port:<5} OPEN  {service}")
            open_ports.append(port)

    duration = time.time() - start_time

    print("\nScan Results")
    print("-" * 30)

    if open_ports:
        open_ports.sort()
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

    print(f"Scan completed in {duration:.2f} seconds\n")


def parse_ports(port_str):
    try:
        if "-" in port_str:
            start, end = map(int, port_str.split("-"))
            return range(start, end + 1)
        else:
            return [int(p.strip()) for p in port_str.split(",")]
    except ValueError:
        print("Invalid port format. Use formats like 80,443 or 1-1024")
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument(
        "-p", "--ports",
        default="21,22,23,25,53,80,110,143,443,445,3389",
        help="Ports (e.g. 80,443 or 1-1024)"
    )
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=50,
        help="Number of threads (default: 50)"
    )

    args = parser.parse_args()

    ports = parse_ports(args.ports)
    scan_host(args.target, ports, args.threads)
