#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("{:d}".format(0))
    else:
        for i in range(1, len(sys.argv)):
            result = 0
            result = int(sys.argv[i]) + result
            print("{:d}".format(result))
