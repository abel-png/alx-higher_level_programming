#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    for k in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(k, a_dictionary[k]))
