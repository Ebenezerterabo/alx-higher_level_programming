#1/bin/bash
# A script that takes in a URL and displays all HTTP methods in the server
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-