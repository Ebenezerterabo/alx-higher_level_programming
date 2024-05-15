#!/usr/bin/python3

"""
A python script that takes in URL and an email, sends a POST request
to the passed URL with the email as a parameter
"""

from urllib.parse import urlencode
from urllib.request import urlopen, Request
from sys import argv

# Encode the data
encode_data = urlencode({'email': argv[2]}).encode('UTF-8')
# Create the request object
req = Request(argv[1], data=encode_data, method="POST")

with urlopen(req) as response:
    email_body = response.read()
    print(f"{email_body.decode('UTF-8')}")
