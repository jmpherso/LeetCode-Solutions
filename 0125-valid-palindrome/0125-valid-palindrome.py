class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        # Thoughts/constraints/edge cases:
        # 1 <= s.length <= 2 * 10^5
        # s consists only of printable ASCII characters.

        # Base case: if the string is empty, return True
        if not s:
            return True

        # Initialize two pointers, one at the beginning and one at the end of the string
        left = 0
        right = len(s) - 1

        # While the left pointer is less than the right pointer
        while left < right:
            # If the left character is not alphanumeric, increment the left pointer
            if not s[left].isalnum():
                left += 1
                continue

            # If the right character is not alphanumeric, decrement the right pointer
            if not s[right].isalnum():
                right -= 1
                continue

            # If the left and right characters are not equal, return False
            if s[left].lower() != s[right].lower():
                return False

            # Increment the left pointer and decrement the right pointer
            left += 1
            right -= 1

        # Return True
        return True
