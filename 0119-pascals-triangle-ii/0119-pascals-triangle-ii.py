class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        # Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

        # Thoughts/constraints/edge cases:
        # Could you optimize your algorithm to use only O(rowIndex) extra space?
        # 0 <= rowIndex <= 33

        # Base case: if rowIndex is 0, return [1]
        if rowIndex == 0:
            return [1]

        # Create a list to store the row
        row = []

        # Create the first row
        row.append(1)

        # Iterate through the rows
        for i in range(1, rowIndex + 1):
            # Add 1 to the beginning of the row
            row.insert(0, 1)

            # Iterate through the row
            for j in range(1, i):
                # Add the sum of the two numbers above the current number to the row
                row[j] = row[j] + row[j + 1]

        # Return the row
        return row

