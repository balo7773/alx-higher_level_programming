#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        print("{:d} {}.".format(len(sys.argv) - 1, "arguments"))
    if len(sys.argv) > 1:
        print("{} {}:".format(len(sys.argv) - 1, "arguements"))
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))