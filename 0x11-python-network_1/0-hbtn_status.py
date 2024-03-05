#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
from urllib import request


if __name__ == "__main__":
	with request.urlopen("https://alx-intranet.hbtn.io/status") as reply:
		body = reply.read()
		print("Body response:")
		print("\t- type: {}".format(type(body)))
		print("\t- content: {}".format(body))
		print("\t- utf8 content: {}".format(body.decode("utf-8")))

