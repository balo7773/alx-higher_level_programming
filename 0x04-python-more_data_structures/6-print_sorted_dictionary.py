#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortd = sorted(a_dictionary)
    for i in sortd:
        print("{}: {}".format(i, a_dictionary[i]))
