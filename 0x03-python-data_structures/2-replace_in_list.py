#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    idxLen = len(my_list) - 1

    if idx < 0 or idx > idxLen:
        return(my_list)

    my_list[idx] = element
    return(my_list)
