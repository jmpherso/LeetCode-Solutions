class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

        # Thoughts/constraints/edge cases:
        # 1. nums is non-empty
        # 2. nums contains only integers
        # 1 <= nums.length <= 3 * 104
        # -3 * 104 <= nums[i] <= 3 * 104
        # Each element in the array appears twice except for one element which appears only once.

        # Base case, nums is length 1
        if len(nums) == 1:
            return nums[0]

        # Sort nums
        nums.sort()

        # Iterate through nums, checking if the current number is equal to the next number
        # If it is, skip the next number
        # If it isn't, return the current number
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] != nums[i + 1]:
                return nums[i]

        # If we get to the end of the loop, return the last number
        return nums[-1]

