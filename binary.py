# Implements operations on binary numbers.
# CSC 225, Assignment 1
# Given code, Spring '22


def add(addend_a, addend_b):
    """
    Add two 16-bit, two's complement numbers; ignore carries/overflows.

    :param addend_a: A bitstring representing the first number
    :param addend_b: A bitstring representing the second number
    :return: A bitstring representing the sum
    """

    bitstring = ""    # create a string to store the bits in
    carry = "0"    # track if a value is being carried over

    # reverse the addends in order to add in the right order
    reverse_a = addend_a[::-1]
    reverse_b = addend_b[::-1]

    for i in range(0, 16):    # iterate through all 16 bits

        if carry == "0":

            if reverse_a[i] == "0" and reverse_b[i] == "0":

                bitstring += "0"
                carry = "0"

            elif reverse_a[i] == "1" and reverse_b[i] == "1":

                bitstring += "0"
                carry = "1"

            elif (reverse_a[i] == "1" and reverse_b[i] == "0") or (reverse_a[i] == "0" and reverse_b[i] == "1"):

                bitstring += "1"
                carry = "0"

        else:    # if carry is "1"

            if reverse_a[i] == "0" and reverse_b[i] == "0":

                bitstring += "1"
                carry = "0"

            elif reverse_a[i] == "1" and reverse_b[i] == "1":

                bitstring += "1"
                carry = "1"

            elif (reverse_a[i] == "1" and reverse_b[i] == "0") or (reverse_a[i] == "0" and reverse_b[i] == "1"):

                bitstring += "0"
                carry = "1"

    # unreverse the bitstring
    bitstring = bitstring[::-1]

    return bitstring


def negate(number):
    """
    Negate a 16-bit, two's complement number.

    :param number: A bitstring representing the number to negate
    :return: A bistring representing the negated number
    """

    bitstring = ""    # create a string to store the bits in

    # iterate through each bit of the number
    # switch 1s to 0s and 0s to 1s
    for i in range(0, 16):

        if number[i] == "1":

            bitstring += "0"

        else:

            bitstring += "1"

    # add the binary of 1 to complete the negation
    bitstring = add(bitstring, "0000000000000001")

    return bitstring


def subtract(minuend, subtrahend):
    """
    Subtract one 16-bit, two's complement number from another.

    :param minuend: A bitstring representing the number from which to subtract
    :param subtrahend: A bitstring representing the number to subtract
    :return: A bitstring representing the difference
    """

    # subtraction is the same as adding a negative
    return add(minuend, negate(subtrahend))


def multiply(multiplicand_a, multiplicand_b):
    """
    Multiply two 16-bit, two's complement numbers; ignore carries/overflows.

    :param multiplicand_a: A bitstring representing the first number
    :param multiplicand_b: A bitstring representing the second number
    :return: A bitstring representing the product
    """

    # I'm not totally sure this function is right... because of multiplying two big numbers...

    bitstring = "0000000000000000"    # create a bitstring of value 0 to start with
    row_list = []    # create an empty list to store values in

    # reverse multiplicands in order to add in the right order
    reverse_a = multiplicand_a[::-1]
    reverse_b = multiplicand_b[::-1]

    # iterate through each bit in the reverse_b
    for i in range(0, 16):

        row = "0" * i    # create placeholder 0s
        # iterate through each bit in the reverse_a
        for j in range(0, 16):

            if reverse_b[i] == "1":

                row += reverse_a[j]

            else:

                row += "0"

        row = row[::-1]    # reverse row so it's in the right order
        row_list.append(row)    # add to row list for later addition

    # add up all the items in the row list
    for r in row_list:

        bitstring = add(bitstring, r)

    return bitstring


def binary_to_decimal(number):
    """
    Convert a 16-bit, two's complement number to decimal.

    :param number: A bitstring representing the number to convert
    :return: An integer, the converted number
    """

    neg = False    # track if binary number given is negative or not

    # if the binary number given is negative negate for calculations
    if number[0] == "1":

        number = negate(number)
        neg = True

    decimal = 0    # create a starting value for the decimal
    reverse = number[::-1]    # reverse number for calculations

    # for each bit of the binary number
    for i in range(0, 16):

        if reverse[i] == "1":

            decimal += 2**i

    # if binary number was originally negative, convert decimal to negative
    if neg:

        return decimal * -1

    return decimal


def decimal_to_binary(number):
    """
    Convert a decimal number to 16-bit, two's complement binary.

    :param number: An integer, the number to convert
    :return: A bitstring representing the converted number
    :raise OverflowError: If the number cannot be represented with 16 bits
    """

    bitstring = ""    # create a string to store the bits in
    neg = False    # track if the decimal number given is negative or not

    # raise overflow error if decimal number cannot be represented with 16 bits
    if number > 32767 or number < -32768:

        raise OverflowError

    # if the decimal number given is negative
    if number < 0:

        number *= -1
        neg = True

    # keep dividing down until 0 is reached
    while number != 0:

        if number % 2 == 0:

            number = number / 2
            bitstring += "0"

        else:

            number = number // 2
            bitstring += "1"

    # if the decimal number was negative, the bits need to be reversed

    bitstring = bitstring[::-1]

    # add extra zeros to the bitstring, so it is length 16
    num = 16 - len(bitstring)
    zeros = "0" * num
    bitstring = zeros + bitstring

    # if the decimal number was negative, negate
    if neg:

        bitstring = negate(bitstring)

    return bitstring
