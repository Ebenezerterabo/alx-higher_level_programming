#!/bin/bash
# A script that sends a JSON POST request to a URL and displays body as response
curl -X POST -sH "content-Type: application/json" -d "("cat "$2")" "$1"
