class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Length of last word in string s, made up of words and spaces.
        # Iterate backwards through the string, make sure to ignore trailing spaces, increment counter until space is reached.

        # Thoughts/constraints/edges:
        # String cannot be empty, at least one word.
        # String may end in a space.

        # Iterate backwards through the string
        for i in range(len(s) - 1, -1, -1):
            # If the current character is not a space
            if s[i] != " ":
                # Iterate backwards through the string again
                for j in range(i, -1, -1):
                    # If the current character is a space
                    if s[j] == " ":
                        # Return the length of the last word
                        return i - j
                # If no spaces were found, return the length of the string
                return i + 1

