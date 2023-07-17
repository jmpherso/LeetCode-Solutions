class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # Add 1 to the last digit of a list of digits, return the list of digits
        # If the last digit is 9, set it to 0 and add 1 to the second to last digit, etc.

        # Thoughts/constraints/edges:
        # Digits are in the range [0, 9]
        # The list cannot be empty
        # No leading 0s.

        # If the list is empty, return the list
        if not digits:
            return digits

        # If the last digit is not 9, add 1 to it and return the list
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        # If the last digit is 9, set it to 0 and add 1 to the second to last digit, etc.
        else:
            # Set the last digit to 0
            digits[-1] = 0
            # Create a pointer to the second to last digit
            pointer = len(digits) - 2
            # Iterate through the list backwards
            while pointer >= 0:
                # If the current digit is 9, set it to 0
                if digits[pointer] == 9:
                    digits[pointer] = 0
                    # Decrement the pointer
                    pointer -= 1
                # If the current digit is not 9, add 1 to it and return the list
                else:
                    digits[pointer] += 1
                    return digits
            # If the pointer is -1, insert a 1 at the beginning of the list and return the list
            digits.insert(0, 1)
            return digits
        
