#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST to the requested
URL with the email as the parameter and displays the response
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode()
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
