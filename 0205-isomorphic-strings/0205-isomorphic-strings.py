class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Given two strings s and t, determine if they are isomorphic.

        # Thoughts/constraints/edge cases:
        # 1 <= s.length <= 5 * 10^4
        # t.length == s.length
        # s and t consist of any valid ascii character

        # Approach 1: Hash Map
        # Time: O(n) Space: O(n)

        # Create hash map
        hash_map = {}

        # Iterate through s and t
        for char_s, char_t in zip(s, t):
            # If char_s is in hash_map
            if char_s in hash_map:
                # If char_t is not equal to hash_map[char_s]
                if char_t != hash_map[char_s]:
                    # Return False
                    return False
            # Else
            else:
                # If char_t is in hash_map.values()
                if char_t in hash_map.values():
                    # Return False
                    return False
                # Set hash_map[char_s] to char_t
                hash_map[char_s] = char_t

        # Return True
        return True
        
