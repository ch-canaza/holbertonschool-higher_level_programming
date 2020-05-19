#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        print("exception:", err, file=sys.stderr)
        return None
    return result
