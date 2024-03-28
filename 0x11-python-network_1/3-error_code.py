#!/usr/bin/python3
"""Takes a url and displays the body of the response"""


if __name__ == "__main__":
    import urllib.error
    import urllib.request
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
