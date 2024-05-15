#!/bin/bash
# A script that sends a JSON POST request to a URL and displays body as response
curl -s -X POST -H "content-Type: application/json" "$1" -d @"$2"
