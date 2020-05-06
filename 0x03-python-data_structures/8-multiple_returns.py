#!/usr/bin/python3
def multiple_returns(sentence):

        len_s = len(sentence)
        if len_s == 0:
            first_c = None
        else:
            first_c = sentence[0]
        return (len_s, first_c)
