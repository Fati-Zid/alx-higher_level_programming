#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
from urllib import request


def fetch_status(url):
    """Fetches the status from the given URL."""
    with request.urlopen(url) as reply:
        body = reply.read()
        return body, body.decode("utf-8")


def print_response_info(content, utf8_content):
    """Prints response information."""
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(utf8_content))


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    content, utf8_content = fetch_status(url)
    print_response_info(content, utf8_content)
    print("\nScore: 0 out of 3 points\nReason:\nAuto fail - project not accessed .")
