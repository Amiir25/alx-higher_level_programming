#!/usr/bin/python3
'''
6-peak.py

This module finds a peak from an unsorted array
'''

def find_peak(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:  # Peak must be on the right
            left = mid + 1
        else:  # Peak is on the left or at mid
            right = mid

    return arr[left]  # left and right converge to a peak
