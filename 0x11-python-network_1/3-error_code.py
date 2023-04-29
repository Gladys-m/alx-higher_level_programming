#!/usr/bin/python3
"""manages urllib.error.HTTPError"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as er:
        print(f'Error code: {er.code}')
