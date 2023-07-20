class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Climb n stairs in any combination of 2 or 1 steps.

        # Thoughts/constraints/edge cases:
        # n is a positive integer between 1 and 45.
        # It's a Fibonacci sequence. 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

        # Create list of Fibonacci sequence up to n.
        fib_list = [1, 2]

        # Create counter for counting up.
        counter = 2

        # Count up until counter is equal to n.
        while counter < n:
            # Add last two numbers in list together.
            fib_list.append(fib_list[-1] + fib_list[-2])

            # Increment counter.
            counter += 1

        # If n == 1, return 1. Else, return last number in list.
        if n == 1:
            return fib_list[0]
        else:
            return fib_list[-1]

