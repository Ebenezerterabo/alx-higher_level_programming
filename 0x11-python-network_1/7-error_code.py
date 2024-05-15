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
    # Print the error code
    print(f'Error code: {error_code}')
