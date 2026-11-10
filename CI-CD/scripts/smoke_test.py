"""Post-deployment validation. Usage: python scripts/smoke_test.py [base_url]"""

import json
import sys
import time
import urllib.error
import urllib.request

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"


def get(path: str) -> dict:
    with urllib.request.urlopen(BASE + path, timeout=5) as resp:  # nosec B310
        return json.load(resp)


def wait_until_healthy(retries: int = 15) -> None:
    for _ in range(retries):
        try:
            if get("/health")["status"] == "ok":
                return
        except (urllib.error.URLError, ConnectionError, TimeoutError):
            pass
        time.sleep(1)
    sys.exit("FAIL: service did not become healthy")


def main() -> None:
    wait_until_healthy()
    if get("/subnet?cidr=10.0.0.0/24")["usable_hosts"] != 254:
        sys.exit("FAIL: subnet check")
    if get("/overlap?a=10.0.0.0/16&b=10.0.1.0/24")["overlap"] is not True:
        sys.exit("FAIL: overlap check")
    print("Smoke tests passed")


if __name__ == "__main__":
    main()
