#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    no_of_printed_element = 0
    for idx in range(0, x):
        try:
            print("{:d}".format(my_list[idx]), end='')
            no_of_printed_element += 1
        except Exception as e:
            break
    print('')
    return no_of_printed_element
