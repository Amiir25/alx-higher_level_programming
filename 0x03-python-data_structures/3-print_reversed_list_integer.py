#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_rev = my_list.copy()
    j = len(my_list) - 1
    for i in range(len(my_list)):
        list_rev[i] = my_list[j]
        print("{:d}".format(list_rev[i]))
        j -= 1
