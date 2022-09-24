#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4 import *

    dicovers_1 = dir(hidden_4)

    for s in dicovers_1[1:]:
	print("{:s}".format(s))
