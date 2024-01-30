#!/bin/bash
# This script takes a URL as an argument, sends a request using curl, and displays the size of the response body in bytes.

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Use curl to send a GET request and display the size of the response body in bytes
SIZE=$(curl -sI "$URL" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')

if [ -z "$SIZE" ]; then
  echo "Error: Unable to retrieve content length."
else
  echo "Correct output: GET $URL => \"$SIZE bytes\""
fi
