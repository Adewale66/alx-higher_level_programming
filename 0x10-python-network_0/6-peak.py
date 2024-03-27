#!/usr/bin/python3
""" Find a peak in a list of integers """

def find_peak(list_of_integers):
    """Find a peak in a list of integers."""
    if not list_of_integers:
        return None
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    mid = n // 2
    if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    return find_peak(list_of_integers[:mid])
