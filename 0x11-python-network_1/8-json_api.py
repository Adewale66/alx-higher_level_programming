#!/usr/bin/python3
"""Takes a letter and sends a POST request to a URL with the letter as a parameter"""

if __name__ == "__main__":
    import requests
    from sys import argv
    
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user" + "?q=" + q
    response = requests.post(url)
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json["id"], json["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
