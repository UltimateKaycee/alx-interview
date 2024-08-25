#!/usr/bin/pythoni3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """
    Function Definition
    Data: integer lists
    Return: Will return True if data is a valid UTF-8
    encoding, otherwise will return false
    """
    countbyte = 0

    for bain in data:
        if countbyte == 0:
            if bain >> 5 == 0b110 or bain >> 5 == 0b1110:
                countbyte = 1
            elif bain >> 4 == 0b1110:
                countbyte = 2
            elif bain >> 3 == 0b11110:
                countbyte = 3
            elif bain >> 7 == 0b1:
                return False
        else:
            if bain >> 6 != 0b10:
                return False
            countbyte -= 1
    return countbyte == 0
