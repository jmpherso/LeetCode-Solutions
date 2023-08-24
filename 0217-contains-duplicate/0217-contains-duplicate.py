class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

        # Thoughts/constraints/edge cases:
        # 1. 1 <= nums.length <= 105
        # 2. -109 <= nums[i] <= 109

        # Approach 1: Brute force
        # Time: O(n^2)

        # Approach 2: Hash table
        # Time: O(n)

        # Create a hash table
        hash_table = {}

        # Iterate through the array
        for num in nums:

                # If the number is in the hash table, return True
                if num in hash_table:
                    return True

                # Else, add the number to the hash table
                else:
                    hash_table[num] = 1

        # If the number is not in the hash table, return False
        return False
        
