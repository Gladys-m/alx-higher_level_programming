#!/usr/bin/python3
""" Function to find a peak in list """

def find_peak(list_of_integers):
    """ Finds a peak in a list of an unsorted array """

    if not list_of_integers:
        return None

    middle_index = len(list_of_integers) // 2
    middle_element = list_of_integers[middle_index]

    if (middle_index == 0 or middle_element >= list_of_integers[middle_index-1]) and \
            (middle_index == len(list_of_integers)-1 or middle_element >= list_of_integers[middle_index+1]):
        return middle_element

    if middle_index > 0 and list_of_integers[middle_index-1] > middle_element:
        return find_peak(list_of_integers[:middle_index])
    else:
        return find_peak(list_of_integers[middle_index+1:])

