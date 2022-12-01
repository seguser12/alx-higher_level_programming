#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_len = len(sys.argv) - 1
    if args_len == 0:
        print("0 arguments.")
    elif args_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_len))
    for args in range(1, len(sys.argv)):
        print("{}: {}".format(args, sys.argv[args]))
