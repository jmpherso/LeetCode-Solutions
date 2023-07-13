class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Longest common prefix of a list of strings
        # If there is no common prefix, return an empty string
        # If there is a common prefix, return the common prefix
        # If the list is empty, return empty string

        # If the list is empty, return empty string
        if not strs:
            return ""

        # If the list contains an empty string, return empty string
        if "" in strs:
            return ""

        # If the list contains one string, return the string
        if len(strs) == 1:
            return strs[0]

        # Iterate through the characters of the first string
        for i in range(len(strs[0])):
            # Iterate through the strings in the list
            for string in strs:
                # If the current index is greater than or equal to the length of the current string or the current character is not equal to the current character of the first string
                if i >= len(string) or string[i] != strs[0][i]:
                    # Return the first string up to the current index
                    return strs[0][:i]
        
        # Return the first string
        return strs[0]
