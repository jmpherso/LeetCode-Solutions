class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Determine if s is a valid string of brackets with rules :
        # Open brackets must be closed by the same type of brackets.
        # Open brackets must be closed in the correct order.
        # Every close bracket has a corresponding open bracket of the same type.

        # Edge cases/constraints/thoughts :
        # If the string is empty, return True
        # If the string is odd, return False
        # If the string contains a character other than a bracket, return False
        # If the string contains an unopened close bracket before an open bracket, return False
        # The brackets must close in order, so a closed bracket most correspond to most recently opened bracket.


        # If the string is empty, return True
        if not s:
            return True

        # If the string is odd, return False
        if len(s) % 2 != 0:
            return False

        # List to use as open bracket stack
        # Closed brackets must use the most recently opened bracket of the same type
        open_brackets = []

        # List of all bracket characters
        brackets = ['(', ')', '[', ']', '{', '}']

        # List of all open brackets
        open_bracket_list = ['(', '[', '{']

        # List of all closed brackets
        closed_bracket_list = [')', ']', '}']

        # Iterate through the string
        for i in range(len(s)):
            # If the current character is not a bracket, return False
            if s[i] not in brackets:
                return False

            # If the current character is an open bracket, append it to the open bracket stack
            if s[i] in open_bracket_list:
                open_brackets.append(s[i])

            # If the current character is a closed bracket
            if s[i] in closed_bracket_list:
                # If the open bracket stack is empty, return False
                if not open_brackets:
                    return False

                # If the current character is not the corresponding closed bracket of the most recently opened bracket, return False
                if s[i] == ')' and open_brackets[-1] != '(':
                    return False
                if s[i] == ']' and open_brackets[-1] != '[':
                    return False
                if s[i] == '}' and open_brackets[-1] != '{':
                    return False

                # If the current character is the corresponding closed bracket of the most recently opened bracket, pop the most recently opened bracket from the open bracket stack
                open_brackets.pop()

        # If the open bracket stack is not empty, return False
        if open_brackets:
            return False
        
        # Return True
        return True
