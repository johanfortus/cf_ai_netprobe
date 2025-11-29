import subprocess
import requests
import re

TARGET_HOST = "8.8.8.8"
WORKER_INGEST_URL = "http://localhost:8787/ingest"


def run_ping(count=5):
    result = subprocess.run(
        # ping -c <count> 8.8.8.8
        ["ping", "-c", str(count), TARGET_HOST],
        capture_output = True,
        text = True
    )
    return result.stdout


def parse_ping(output: str):
    times = []
    for line in output.splitlines():
        match = re.search(r"time=([\d\.]+)\s*ms", line)
        if match:
            times.append(float(match.group(1)))

    avg_latency = sum(times) / len(times) if times else None

    if len(times) >= 2:
        jitter = max(times) - min(times)
    else:
        jitter = 0.0

    packet_loss = None
    for line in output.splitlines():
        if "packet loss" in line:
            m = re.search(r"(\d+)% packet loss", line)
            if m:
                packet_loss = float(m.group(1))
            break

    return {
        "latency": avg_latency,
        "jitter": jitter,
        "packet_loss": packet_loss,
    }


def send_measurement(measurement: dict):
    resp = requests.post(
        WORKER_INGEST_URL,
        json=measurement,
        timeout=5
    )
    print("Ingest response:", resp.status_code, resp.text)


def main():
    output = run_ping()
    measurement = parse_ping(output)
    print("Measurement:", measurement)

    if measurement["latency"] is not None:
        send_measurement(measurement)
    else:
        print("No valid latency parsed, skip send.")


if __name__ == "__main__":
    main()