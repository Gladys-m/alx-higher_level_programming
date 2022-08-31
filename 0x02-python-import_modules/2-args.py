#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv)
    if length == 1:
        print(f"{length - 1} arguments.")
    elif length == 2:
        print(f"{length - 1} argument:")
    else:
        print(f"{length - 1} arguments:")
    for i in range(1,length):
        args = (argv[i])
        print(f"{i}: {args}")

