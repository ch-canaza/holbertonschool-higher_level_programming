#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("{:d} arguments.".format(0))
    else:
        print("{:d} arguments:".format(len(sys.argv)- 1))
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
