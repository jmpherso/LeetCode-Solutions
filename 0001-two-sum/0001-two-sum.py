class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index, num in enumerate(nums):
            if target - num in nums and nums.index(target - num) != index:
                return [index, nums.index(target - num)]
        
