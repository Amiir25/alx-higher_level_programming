#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        if count == x:
            break

        try:
            if i >= 0 or i <= 9:
                print("{:d}".format(i), end='')

        except TypeError:
            print("Error: Non integer value")

        count += 1

    print("")

    return count
