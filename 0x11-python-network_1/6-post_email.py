#!/usr/bin/python3

"""
A script that takes in a URL and an email address, sends a POST request
to the passed URL with the email  as a parameter and display the response
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}

    # Get response
    reponse = requests.post(url, data=data)
    # Convert response to string(Body)
    response_str = reponse.text

    print(response_str)
