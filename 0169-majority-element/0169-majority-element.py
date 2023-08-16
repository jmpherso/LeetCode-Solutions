class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Given an array nums of size n, return the majority element.

        # Thoughts/constraints/edge cases:
        # n == nums.length
        # 1 <= n <= 5 * 10^4
        # -2^31 <= nums[i] <= 2^31 - 1
        # It is guaranteed that the majority element exists in the array.

        # Approach 1: Hashmap
        # Time: O(n) Space: O(n)

        # Create hashmap
        hashmap = {}

        # Iterate through nums
        for num in nums:
            # If num is in hashmap, increment value
            if num in hashmap:
                hashmap[num] += 1
            # Else, add num to hashmap with value 1
            else:
                hashmap[num] = 1

        # Iterate through hashmap
        for key, value in hashmap.items():
            # If value is greater than n // 2, return key
            if value > len(nums) // 2:
                return key

        # Return None
        return None
