import subprocess
import requests

TARGET_HOST = "8.8.8.8"


def run_ping(count=5):
    result = subprocess.run(
        # ping -c <count> 8.8.8.8
        ["ping", "-c", str(count), TARGET_HOST],
        capture_output = True,
        text = True
    )
    return result.stdout


def main():
    output = run_ping()
    print(output)


if __name__ == "__main__":
    main()