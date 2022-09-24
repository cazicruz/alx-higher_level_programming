#!/usr/bin/python3

if __name__ == "__main__":
    """Print sum of arguments."""
    import sys

    count = len(sys.argv) - 1

    for i in range(count):
	sum +=int( sys.argv[i+1])

    print("{}".format(sum))
