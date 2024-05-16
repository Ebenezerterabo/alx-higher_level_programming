#!/usr/bin/python3

"""
A script  that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'

    username = argv[1]
    password = argv[2]

    response = requests.get(url, auth=(username, password))
    json_response = response.json()
    print(json_response.get('id'))
