#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            x_request_id = response.getheader("X-Request-Id")
            if x_request_id:
                print(x_request_id)
    except urllib.error.HTTPError as e:
        if hasattr(e, 'headers') and 'X-Request-Id' in dict(e.headers):
            print(e.headers['X-Request-Id'])
        else:
            print("No X-Request-Id found in HTTP headers.")
