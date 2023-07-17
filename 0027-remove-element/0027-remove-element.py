class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # Return all instances of val in nums, return original length - number of instances of val.
        # Items should be shifted down when val is removed. Do not allocate extra space for another array.
        # Places beyond the end of original array numbers can be anything.
        # True length after removal doesn't matter, just need original length minus removed items.

        # Thoughts/constraints/edges:
        # Array is not sorted.
        # Array can be empty. If array is empty, return 0.
        # Array cannot contain negative numbers.

        # If the array is empty, return 0
        if not nums:
            return 0

        # If the array contains one number
        if len(nums) == 1:
            # If the number is equal to val, return 0
            if nums[0] == val:
                return 0
            # If the number is not equal to val, return 1
            else:
                return 1

        # Create a pointer to the first number
        pointer = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current number is not equal to val
            if nums[i] != val:
                # Set the number at the pointer to the current number
                nums[pointer] = nums[i]
                # Increment the pointer
                pointer += 1

        # Return the pointer
        return pointer
        
