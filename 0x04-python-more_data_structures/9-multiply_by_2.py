#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = dict()
    k = 0
    for i, j in sorted(a_dictionary.items()):
        new_dic[i] = j * 2
    return new_dic
