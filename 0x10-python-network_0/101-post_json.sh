#!/bin/bash
# A script that sends a JSON POST request to a URL and displays body as response
curl -X POST -H "content-Type: application/json" -d "$2" "$1"
