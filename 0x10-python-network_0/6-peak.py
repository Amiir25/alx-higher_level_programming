#!/usr/bin/python3
'''
6-peak.py

This module finds a peak from a list unsorted integers
'''


def find_peak(list_of_integers):
    '''Finds a peak from a list of integers'''

    if not list_of_integers:
        return None

    arr = list_of_integers
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:  # Peak must be on the right
            left = mid + 1
        else:  # Peak is on the left or at mid
            right = mid

    return arr[left]  # left and right converge to a peak
