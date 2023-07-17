class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Remove duplicates from a sorted array of integers, return length of array after removal.

        # Thoughts/constraints/edges:
        # Array is sorted ascending
        # Array cannot be empty (minimum 1 number). If length is 1, return 1.
        # Array can contain negative numbers

        # If the array is empty, return 0
        if not nums:
            return 0

        # If the array contains one number, return 1
        if len(nums) == 1:
            return 1

        # Create a pointer to the first number
        pointer = 0

        # Iterate through the array
        for i in range(1, len(nums)):
            # If the current number is not equal to the number at the pointer
            if nums[i] != nums[pointer]:
                # Increment the pointer
                pointer += 1
                # Set the number at the pointer to the current number
                nums[pointer] = nums[i]

        # Return the pointer + 1
        return pointer + 1
