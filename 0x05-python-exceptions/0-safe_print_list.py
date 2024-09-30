#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0;

    try:
        for i in my_list:
            if count == x:
                break;

            if i >= 0 or i <= 9:
                print("{:d}".format(i), end='')
                count += 1
        print("")

    except:
        print("Unknown Error");

    return count
