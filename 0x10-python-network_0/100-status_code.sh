#!/bin/bash
# A script that sends a request to a URL and displays the status code
curl -o /dev/null -s -w "%{http_code}" "$1"