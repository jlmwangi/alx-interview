#!/usr/bin/python3
'''determine if a given data set represents a valid utf8-encoding'''


def validUTF8(data):
    '''return true if valid utf8, false if not'''
    n_bytes = 0  # keeeps track of how many continuation bytes are expected
    for num in data:  # go through each item in list
        if n_bytes == 0:
            if (num >> 7 == 0b0):  # Single byte sequence
                continue
            elif (num >> 5 == 0b110):  # 2-byte sequence
                n_bytes = 1
            elif (num >> 4 == 0b1110):  # 3-byte sequence
                n_bytes = 2
            elif (num >> 3 == 0b11110):  # 4-byte sequence
                n_bytes = 3
            else:
                return False
        else:
            if (num >> 6 != 0b10):
                return False
            n_bytes -= 1

    return n_bytes == 0
