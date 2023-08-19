class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

        # Thoughts/constraints/edge cases:
        # 0 <= n <= 2^31 - 1

        # Approach 1: Bit Manipulation
        # Time: O(1) Space: O(1)

        # Create output
        output = 0

        # Iterate through 32 bits
        for i in range(32):
            # Add last bit of n to output
            output += n & 1
            # Shift n right
            n >>= 1

        # Return output
        return output
