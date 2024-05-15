#!/usr/bin/python3

"""
A script that takes in a letter and sends a POST request to url with
letter as parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Post request
    url = "http://0.0.0.0:5000/search_user"

    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""

    response = requests.post(url, data={'q': q})
    try:
        json_response = response.json()
        if json_response:
            print(f'[{json_response.get('id')}] {json_response.get('name')}')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
