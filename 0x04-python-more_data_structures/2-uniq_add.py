#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_ints = set()
    # Iterate over the elements in the list
    for elem in my_list:
        # Add the element to the set if it hasn't been added before
        if elem not in unique_ints:
            unique_ints.add(elem)
    # Compute the sum of the unique integers and return it
    return sum(unique_ints)
