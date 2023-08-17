class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        # Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

        # Thoughts/constraints/edge cases:
        # 1 <= columnTitle.length <= 7
        # columnTitle consists only of uppercase English letters.
        # columnTitle is in the range ["A", "FXSHRXW"].
        # A = 1, Z = 26, AA = 27, AB = 28, ...

        # Approach 1: Iterative
        # Time: O(n) Space: O(1)

        # Create dictionary
        alphabet = {chr(i + 64): i for i in range(1, 27)}

        # Create output
        output = 0

        # Iterate through columnTitle
        for i in range(len(columnTitle)):
            # Get value of letter
            value = alphabet[columnTitle[i]]
            # Update output
            output += value * (26 ** (len(columnTitle) - i - 1))

        # Return output
        return output
