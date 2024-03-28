#!/usr/bin/python3
"""Takes a url and displays the body of the response"""


if __name__ == "__main__":
    import urllib
    from sys import argv

    try:
        req = urllib.request.Request(argv[1])
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
