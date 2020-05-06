#!/usr/bin/python3
def max_integer(my_list=[]):
    len_l = len(my_list)
    greatest = 0
    if len_l == 0:
        return None
    for i in my_list:
        if i > greatest:
            greatest = i
    return (greatest)
