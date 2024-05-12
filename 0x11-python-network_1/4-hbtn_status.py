#!/usr/bin/python3
"""
A python script that fetches URL
"""
import requests

# URL data
url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
# Convert response to string
response_str = response.text
print('Body response:')
print(f'\t- type: {type(response_str)}')
print(f'\t- content: {response_str}')
