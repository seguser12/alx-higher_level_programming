#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum_arg = 0
    for num in range(1, len(sys.argv)):
        sum_arg += eval(sys.argv[num])
    print(sum_arg)
