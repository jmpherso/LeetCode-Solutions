class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # Given two binary strings a and b, return their sum as a binary string.

        # Thoughts/edges/constraints:
        # 1 <= a.length, b.length <= 10^4
        # a and b consist only of '0' or '1' characters.
        # Each string does not contain leading zeros except for the zero itself.

        # Convert to int, add, convert to binary, return

        # Convert to int
        a_int = int(a, 2)
        b_int = int(b, 2)

        # Add
        input_sum = a_int + b_int

        # Convert sum back to binary
        input_sum = bin(input_sum)
        
        # Remove 0b binary signifier from start of string
        input_sum = input_sum[2:]

        # Return conversion
        return input_sum






