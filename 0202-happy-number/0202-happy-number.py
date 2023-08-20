class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # Write an algorithm to determine if a number n is happy.

        # Thoughts/constraints/edge cases:
        # 1 <= n <= 2^31 - 1

        # Approach 1: Hash Set
        # Time: O(logn) Space: O(logn)

        # Create seen set
        seen = set()

        # Iterate until n is 1 or seen
        while n != 1 and n not in seen:
            # Add n to seen
            seen.add(n)
            # Create new n
            new_n = 0
            # Iterate through digits of n
            while n:
                # Add square of last digit to new_n
                new_n += (n % 10) ** 2
                # Shift n right
                n //= 10
            # Set n to new_n
            n = new_n

        # Return True if n is 1
        return n == 1
        
