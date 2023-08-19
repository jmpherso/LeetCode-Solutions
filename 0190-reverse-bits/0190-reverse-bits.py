class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        # Given a non-negative integer n, reverse the bits of n.

        # Thoughts/constraints/edge cases:
        # 0 <= n <= 2^32 - 1

        # Approach 1: Bit Manipulation
        # Time: O(1) Space: O(1)

        # Create output
        output = 0

        # Iterate through 32 bits
        for i in range(32):
            # Shift output left
            output <<= 1
            # Add last bit of n to output
            output |= n & 1
            # Shift n right
            n >>= 1

        # Return output
        return output
