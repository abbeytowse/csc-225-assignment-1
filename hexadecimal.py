# Implements operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given code, Winter '20


def binary_to_hex(number):
    """
    Convert a 16-bit binary number to hexadecimal.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to convert
    :return: A hexadecimal string, the converted number
    """

    # create the starting convention for the hexadecimal
    hexadecimal = "0x"

    # split the binary number into 4 groups of 4
    group1 = number[0:4]
    group2 = number[4:8]
    group3 = number[8:12]
    group4 = number[12:16]

    # put all 4 groups into a list
    groups = [group1, group2, group3, group4]

    # iterate through each group and convert
    for group in groups:

        if group == "0000":

            hexadecimal += "0"

        elif group == "0001":

            hexadecimal += "1"

        elif group == "0010":

            hexadecimal += "2"

        elif group == "0011":

            hexadecimal += "3"

        elif group == "0100":

            hexadecimal += "4"

        elif group == "0101":

            hexadecimal += "5"

        elif group == "0110":

            hexadecimal += "6"

        elif group == "0111":

            hexadecimal += "7"

        elif group == "1000":

            hexadecimal += "8"

        elif group == "1001":

            hexadecimal += "9"

        elif group == "1010":

            hexadecimal += "A"

        elif group == "1011":

            hexadecimal += "B"

        elif group == "1100":

            hexadecimal += "C"

        elif group == "1101":

            hexadecimal += "D"

        elif group == "1110":

            hexadecimal += "E"

        elif group == "1111":

            hexadecimal += "F"

    return hexadecimal


def hex_to_binary(number):
    """
    Convert a hexadecimal number to 16-bit binary.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A hexadecimal string, the number to convert
    :return: A bitstring representing the converted number
    """

    # create a bitstring to store values in
    bitstring = ""

    # split the hexadecimal number into 4 characters
    char1 = number[2]
    char2 = number[3]
    char3 = number[4]
    char4 = number[5]

    # put all 4 characters into a list
    groups = [char1, char2, char3, char4]

    # iterate through each character and convert
    for char in groups:

        if char == "0":

            bitstring += "0000"

        elif char == "1":

            bitstring += "0001"

        elif char == "2":

            bitstring += "0010"

        elif char == "3":

            bitstring += "0011"

        elif char == "4":

            bitstring += "0100"

        elif char == "5":

            bitstring += "0101"

        elif char == "6":

            bitstring += "0110"

        elif char == "7":

            bitstring += "0111"

        elif char == "8":

            bitstring += "1000"

        elif char == "9":

            bitstring += "1001"

        elif char == "A":

            bitstring += "1010"

        elif char == "B":

            bitstring += "1011"

        elif char == "C":

            bitstring += "1100"

        elif char == "D":

            bitstring += "1101"

        elif char == "E":

            bitstring += "1110"

        elif char == "F":

            bitstring += "1111"

    return bitstring
