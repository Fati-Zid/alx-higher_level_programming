#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
