class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Search insert position of a target in a sorted array of unique integers

        # Thoughts/constraints/edges:
        # Array is sorted ascending
        # Array cannot be empty (minimum 1 number). If length is 1 and target is in array, return 0.
        # If length is one and target is less than the number in the array, return 0. If length is one and target is greater than the number in the array, return 1.
        # Array can contain negative numbers

        # If the array is empty, return 0
        if not nums:
            return 0

        # If the array contains one number
        if len(nums) == 1:
            # If the target is less than the number in the array, return 0
            if target <= nums[0]:
                return 0
            # If the target is greater than the number in the array, return 1
            else:
                return 1

        # Create a pointer to the first number
        pointer = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current number is equal to the target, return the pointer
            if nums[i] == target:
                return i
            # If the current number is greater than the target
            elif nums[i] > target:
                # Return the pointer
                return pointer
            # If the current number is less than the target
            else:
                # Increment the pointer
                pointer += 1

        # Return the pointer
        return pointer

