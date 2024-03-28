#!/usr/bin/python3
"""Takes a url and displays the body of the response"""


if __name__ == "__main__":
    import urllib.error
    import urllib.request
    from sys import argv

    try:
        req = urllib.request.Request(argv[1])
        with urllib.request.urlopen(req) as response:
            print(response.read())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
