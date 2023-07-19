import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Create square root function that doesn't use ** operator

        # Thoughts/constraints/edge cases:
        # x can be 0. If x is 0, return 0.
        # x is greater than or equal to 0 (positive).
        # If x is less than 1, return 0.

        # If x is 1, return 1.
        if x == 1:
            return 1

        # If x under 1, return 0.
        if x < 1:
            return 0

        # Create counter for counting up.
        counter = 1

        # Count up until counter squared is greater than x.
        while counter * counter <= x:
            counter += 1

        # Return counter - 1.
        return counter - 1

