#!/usr/bin/python3
"""Module containing function to calculate the fewest number of
operations needed to achieve exactly n 'H' characters"""


def minOperations(n):
    """Function returns integer with minimum number of operations
    required to obtain exactly n 'H' characters in a file"""
    operations = 0
    min_operations = 2

    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1

    return operations
