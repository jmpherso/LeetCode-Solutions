class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        # Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

        # Thoughts/constraints/edge cases:
        # 1 <= columnNumber <= 2^31 - 1
        # A = 1, Z = 26, AA = 27, AB = 28, ...

        # Approach 1: Iterative
        # Time: O(n) Space: O(n)

        # Create dictionary
        alphabet = {i: chr(i + 64) for i in range(1, 27)}

        # Create output string
        output = ""

        # Iterate through columnNumber
        while columnNumber > 0:
            # Get remainder
            remainder = columnNumber % 26
            # If remainder is 0, set remainder to 26
            if remainder == 0:
                remainder = 26
            # Add letter to output
            output = alphabet[remainder] + output
            # Update columnNumber
            columnNumber = (columnNumber - remainder) // 26

        # Return output
        return output

