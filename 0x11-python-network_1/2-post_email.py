#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the header
    of the response.
    * You must use the packages urllib and sys
    * You are not allow to import packages other than urllib and sys
    * The value of this variable is different for each request
    * You don’t need to check arguments passed to the script (number or type)
    * You must use a with statement
"""
import urllib.request as rq
from sys import argv
import urllib.parse as parse

if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}
    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = rq.Request(url, data)
    with rq.urlopen(req) as response:
        print(response.read().decode('utf-8'))
