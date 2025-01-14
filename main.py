import requests
import yaml
import time
from collections import defaultdict
from threading import Thread


def read_config(file_path):
    """Read and parse the YAML configuration file."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


def check_endpoint(endpoint, domain_results):
    """
    Check the health of a single endpoint and update the domain results.
    An endpoint is UP if the response code is 2xx and latency is < 500 ms.
    """
    url = endpoint['url']
    domain = url.split("//")[1].split("/")[0]  # Extract domain from URL
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)

    try:
        start_time = time.time()
        response = requests.request(method, url, headers=headers, data=body, timeout=2)
        latency = (time.time() - start_time) * 1000  # Convert to milliseconds

        if 200 <= response.status_code < 300 and latency < 500:
            domain_results[domain]['up'] += 1
        else:
            domain_results[domain]['down'] += 1
    except requests.RequestException:
        domain_results[domain]['down'] += 1


def log_availability(domain_results):
    """Log the cumulative availability percentage for each domain."""
    for domain, stats in domain_results.items():
        total = stats['up'] + stats['down']
        availability = round(100 * stats['up'] / total) if total > 0 else 0
        print(f"{domain} has {availability}% availability percentage")


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_config_file>")
        return

    config_file = sys.argv[1]
    endpoints = read_config(config_file)

    # Dictionary to store domain-specific results
    domain_results = defaultdict(lambda: {'up': 0, 'down': 0})

    try:
        while True:
            threads = []
            for endpoint in endpoints:
                thread = Thread(target=check_endpoint, args=(endpoint, domain_results))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            log_availability(domain_results)
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nExiting program.")


if __name__ == "__main__":
    main()
