#!/usr/bin/python3
"""
A python script that takes in a URL, sends a request to the URL and displays
the value of the variable in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)

    # Get the variable
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
