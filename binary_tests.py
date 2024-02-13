# Tests operations on binary numbers.
# CSC 225, Assignment 1
# Given tests, Spring '22

import unittest
import binary as bn


class TestBinary(unittest.TestCase):
    def test01_add(self):
        msg = "Testing basic binary addition"
        self.assertEqual(
         bn.add("0000000000000011", "0000000000000010"),
         "0000000000000101", msg)

    def test01_add2(self):
        msg = "Testing more complex binary addition"
        self.assertEqual(bn.add("0001111100100101", "1100111000010101"),
                         "1110110100111010", msg)

    def test02_negate(self):
        msg = "Testing basic binary negation"
        self.assertEqual(
         bn.negate("0000000000000001"),
         "1111111111111111", msg)

    def test02_negate2(self):
        msg = "Testing more complex binary negation"
        self.assertEqual(bn.negate("1110110100111010"),
                         "0001001011000110", msg)

    def test03_subtract(self):
        msg = "Testing basic binary subtraction"
        self.assertEqual(
         bn.subtract("0000000000000011", "0000000000000010"),
         "0000000000000001", msg)

    def test03_subtract2(self):
        msg = "Testing more complex binary subtraction"
        self.assertEqual(bn.subtract("0001111100100101", "1110110100111010"),
                         "0011000111101011", msg)

    def test04_multiply(self):
        msg = "Testing basic binary multiplication"
        self.assertEqual(
         bn.multiply("0000000000000100", "0000000000000101"),
         "0000000000010100", msg)

    # don't like this test... don't know if its right
    def test04_multiply2(self):
        msg = "Testing large number binary multiplication"
        self.assertEqual(bn.multiply("0100111110110100", "1001001000001111"),
                         "0101001110001100", msg)

    def test04_multiply3(self):
        msg = "Testing binary multiplication"
        self.assertEqual(bn.multiply("0000000000000111", "0000000000010100"),
                         "0000000010001100", msg)

    def test04_multiply4(self):
        msg = "Testing binary multiplication"
        self.assertEqual(bn.multiply("0000000000101010", "0000000001100110"),
                         "0001000010111100", msg)

    def test04_multiply5(self):
        msg = "Testing two negatives binary multiplication"
        self.assertEqual(bn.multiply("1111111111111101", "1111111111111011"),
                         "0000000000001111", msg)

    def test04_multiply6(self):
        msg = "Testing 1 negative and 1 positive binary multiplication"
        self.assertEqual(bn.multiply("1111111111110100", "0000000000010001"),
                         "1111111100110100", msg)

    def test04_multiply7(self):
        msg = "Testing 1 binary multiplication with 0"
        self.assertEqual(bn.multiply("1111111111110100", "0000000000000000"),
                         "0000000000000000", msg)

    def test04_multiply8(self):
        msg = "Testing zero times zero binary multiplication"
        self.assertEqual(bn.multiply("0000000000000000", "0000000000000000"),
                         "0000000000000000", msg)

    def test05_binary_to_decimal(self):
        msg = "Testing basic binary-to-decimal conversion"
        self.assertEqual(
         bn.binary_to_decimal("0000000000000101"),
         5, msg)

    def test05_binary_to_decimal2(self):
        msg = "Testing negative binary-to-decimal conversion"
        self.assertEqual(
         bn.binary_to_decimal("1111111111111100"),
         -4, msg)

    def test05_binary_to_decimal3(self):
        msg = "Testing binary-to-decimal of 0"
        self.assertEqual(
         bn.binary_to_decimal("0000000000000000"),
         0, msg)

    def test06_decimal_to_binary(self):
        msg = "Testing basic decimal-to-binary conversion"
        self.assertEqual(
         bn.decimal_to_binary(5),
         "0000000000000101", msg)

    def test06_decimal_to_binary2(self):
        msg = "Testing more complex decimal-to-binary conversion"
        self.assertEqual(
         bn.decimal_to_binary(27),
         "0000000000011011", msg)

    def test06_decimal_to_binary3(self):
        msg = "Testing max decimal-to-binary conversion"
        self.assertEqual(
         bn.decimal_to_binary(32767),
         "0111111111111111", msg)

    def test06_decimal_to_binary4(self):
        msg = "Testing error raised  decimal-to-binary conversion"
        with self.assertRaises(OverflowError, msg=msg):
            bn.decimal_to_binary(32768)

    def test06_decimal_to_binary5(self):
        msg = "Testing basic negative decimal-to-binary conversion"
        self.assertEqual(
            bn.decimal_to_binary(-1),
            "1111111111111111", msg)

    def test06_decimal_to_binary6(self):
        msg = "Testing more complex negative decimal-to-binary conversion"
        self.assertEqual(
            bn.decimal_to_binary(-18),
            "1111111111101110", msg)

    def test06_decimal_to_binary7(self):
        msg = "Testing decimal-to-binary conversion of 0"
        self.assertEqual(
            bn.decimal_to_binary(0),
            "0000000000000000", msg)

    def test06_decimal_to_binary8(self):
        msg = "Testing decimal-to-binary conversion of 0"
        self.assertEqual(
            bn.decimal_to_binary(5533),
            "0001010110011101", msg)

    def test06_decimal_to_binary9(self):
        msg = "Testing decimal-to-binary conversion of 0"
        self.assertEqual(
            bn.decimal_to_binary(32767),
            "0111111111111111", msg)

    def test06_decimal_to_binary10(self):
        msg = "Testing decimal-to-binary conversion of 0"
        self.assertEqual(
            bn.decimal_to_binary(11882),
            "0010111001101010", msg)

    def test06_decimal_to_binary11(self):
        msg = "Testing decimal-to-binary conversion of 0"
        self.assertEqual(
            bn.decimal_to_binary(-32768),
            "1000000000000000", msg)

    def test06_decimal_to_binary12(self):
        msg = "Testing error raised  decimal-to-binary conversion"
        with self.assertRaises(OverflowError, msg=msg):
            bn.decimal_to_binary(-32769)


if __name__ == "__main__":
    unittest.main()
