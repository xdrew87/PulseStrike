import requests
import time
import random
from utils import log_request

def run_test(url, method, delay, user_agents):
    while True:
        headers = {
            "User-Agent": random.choice(user_agents),
            "X-Forwarded-For": f"192.168.{random.randint(1,254)}.{random.randint(1,254)}"
        }

        try:
            if method == "GET":
                r = requests.get(url, headers=headers, timeout=5)
            elif method == "POST":
                r = requests.post(url, headers=headers, data={"test": "pulse"}, timeout=5)
            elif method == "HEAD":
                r = requests.head(url, headers=headers, timeout=5)
            log_request(url, r.status_code, method)
        except requests.RequestException as e:
            log_request(url, "FAIL", method, error=str(e))

        time.sleep(delay)
