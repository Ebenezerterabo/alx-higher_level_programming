#!/usr/bin/python3
"""
Takes URL sends a request to the url and displays the value of the
X-Request variable found in the header of the response
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        request_id = response.headers.get('X-Request-Id')
    print(request_id)
