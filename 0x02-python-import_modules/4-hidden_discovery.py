#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for counter in names:
        if counter[:2] != "__":
            print(counter)
