#!/usr/bin/python3
"""Module containing script that reads stdin line by line
and computes metrics"""
import sys


def print_outcome(sc_dict, total_file_size):
    """
    Function for method to print
    Args:
        sc_dict: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for k, v in sorted(sc_dict.items()):
        if v != 0:
            print("{}: {}".format(k, v))


total_file_size = 0
s_code = 0
counter = 0
sc_dict = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])
                s_code = parsed_line[1]

                if (s_code in sc_dict.keys()):
                    sc_dict[s_code] += 1

            if (counter == 10):
                print_outcome(sc_dict, total_file_size)
                counter = 0

finally:
    print_outcome(sc_dict, total_file_size)
