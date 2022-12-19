#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    no_of_printed_elements = 0
    for idx in range(0, x):
        try:
            print("{:d}". format(my_list[1]), end='')
            no_of_printed_elements += 1
        except (ValueError, TypeError):
            pass
    print()
    return no_of_printed_elements
