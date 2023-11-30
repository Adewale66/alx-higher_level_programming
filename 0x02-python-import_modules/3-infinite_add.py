#!/usr/bin/python3
def add_args(argv):
    sum = 0
    for i in argv[1:]:
        sum += int(i)
    print(sum)


if __name__ == "__main__":
    import sys
    add_args(sys.argv)
