class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Given an array prices where prices[i] is the price of a given stock on the ith day, return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        # Thoughts/constraints/edge cases:
        # 1 <= prices.length <= 10^5
        # 0 <= prices[i] <= 10^4
        # The answer is guaranteed to fit in a 32-bit signed integer.
        # The maximum profit is the maximum difference between two elements in the array, where the second element is greater than the first element.

        # Base case: if prices is empty, return 0
        if not prices:
            return 0

        # Create a variable to store the maximum profit
        max_profit = 0

        # Create a variable to store the minimum price
        min_price = prices[0]

        # Iterate through the prices
        for price in prices:
            # If the current price is less than the minimum price
            if price < min_price:
                # Update the minimum price
                min_price = price
            # Otherwise, if the difference between the current price and the minimum price is greater than the maximum profit
            elif price - min_price > max_profit:
                # Update the maximum profit
                max_profit = price - min_price

        # Return the maximum profit
        return max_profit
