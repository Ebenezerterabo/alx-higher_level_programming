#!/usr/bin/python3

"""
A script that takes in a URL, sends a request to the URL and displays
the body of the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Get the response
    response = requests.get(argv[1])
    # Get the response status codde
    error_code = response.status_code
    # Check and Print the status code
    if error_code == 200:
        print("Index")
    else:
        print(f'Error code: {error_code}')
