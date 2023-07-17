class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # First occurrence of a string in another string

        # Thoughts/constraints/edges:
        # If the needle is empty, return 0
        # If the needle is not in the haystack, return -1
        # If the needle is in the haystack, return the index of the first occurrence

        # If the needle is empty, return 0
        if not needle:
            return 0

        # If the needle is not in the haystack, return -1
        if needle not in haystack:
            return -1

        # If the needle is in the haystack, return the index of the first occurrence
        return haystack.index(needle)

    
