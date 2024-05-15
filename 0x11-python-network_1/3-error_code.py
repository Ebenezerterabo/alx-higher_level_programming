#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and displays
the body of the response
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    import urllib.error
    from sys import argv

    try:
        with urlopen(argv[1]) as response:
            data = response.read()
            print(f'{data.decode('UTF-8')}')
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
