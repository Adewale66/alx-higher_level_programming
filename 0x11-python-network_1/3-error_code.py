#!/usr/bin/python3
"""Takes a url and displays the body of the response"""


if __name__ == "__main__":
    import urllib
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
