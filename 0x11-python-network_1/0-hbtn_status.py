#!/usr/bin/python3
"""
Fetch resource from webserver
"""

from urllib.request import urlopen

if __name__ == "__main__":
    # The URL
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        data = response.read()
    print(f'Body response:')
    print(f'\t- type: {type(data)}')
    print(f'\t- content: {data}')
    print(f"\t-utf8 content: {data.decode('UTF-8')}")
