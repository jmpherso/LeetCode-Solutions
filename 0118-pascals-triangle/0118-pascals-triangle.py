class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # Given an integer numRows, return the first numRows of Pascal's triangle.

        # Thoughts/constraints/edge cases:
        # Pascal's triangle is a triangular array of integers constructed with the following formula:
        # The first row consists of the number 1.
        # For each subsequent row, each element is the sum of the numbers directly above it, on either side.
        # 1 <= numRows <= 30

        # Base case: if numRows is 0, return an empty list
        if numRows == 0:
            return []

        # Create a list of lists to store the triangle
        triangle = []

        # Create the first row
        triangle.append([1])

        # Iterate through the rows
        for i in range(1, numRows):
            # Create the row
            row = []

            # Add 1 to the beginning of the row
            row.append(1)

            # Iterate through the previous row
            for j in range(1, i):
                # Add the sum of the two numbers above the current number to the row
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            # Add 1 to the end of the row
            row.append(1)

            # Add the row to the triangle
            triangle.append(row)

        # Return the triangle
        return triangle
