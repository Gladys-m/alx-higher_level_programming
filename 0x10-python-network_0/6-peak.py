#!/usr/bin/python3
""" Function to find a peak in list """


def find_peak(list_of_integers):
    """ Finds a peak in a list of an unsorted array """

    list_n = list_of_integers

    if not list_n:
        return None

    mid_index = len(list_n) // 2
    mid_element = list_n[mid_index]

    if (mid_index == 0 or mid_element >= list_n[mid_index-1]) and \
            (mid_index == len(list_n)-1 or mid_element >= list_n[mid_index+1]):
        return mid_element

    if mid_index > 0 and list_n[mid_index-1] > mid_element:
        return find_peak(list_n[:mid_index])
    else:
        return find_peak(list_n[mid_index+1:])
