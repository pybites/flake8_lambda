import argparse
import os

import requests

GATEWAY_URL = "https://YOUR_AWS_ID.execute-api.us-east-2.amazonaws.com/v1"


def run_flake8(url):
    payload = {'url': url}
    resp = requests.post(GATEWAY_URL, json=payload)
    resp.raise_for_status()
    return resp.json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run flake8 against a code file')
    parser.add_argument('-u', '--url', help='URL of Python script', required=True)

    args = parser.parse_args()
    url = args.url

    ret = run_flake8(url)

    print(f"Running flake8 against {os.path.basename(url)}:\n")

    for line in ret['body'].strip('"').split("\\n"):
        print(line)
