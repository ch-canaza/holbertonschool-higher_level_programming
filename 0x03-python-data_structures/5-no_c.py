#!/usr/bin/python3
def no_c(my_string):
    rem_c = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        rem_c = rem_c + i
    return rem_c
