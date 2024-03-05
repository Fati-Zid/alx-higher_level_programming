#!/usr/bin/python3
import urllib.request


def fetch_url(url):
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
    return content, utf8_content


def print_response_info(content, utf8_content):
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", utf8_content)


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    content, utf8_content = fetch_url(url)
    print_response_info(content, utf8_content)
