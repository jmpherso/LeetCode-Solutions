class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

        # Thoughts/constraints/edge cases:
        # nums1.length == m + n
        # nums2.length == n
        # 0 <= m, n <= 200
        # 1 <= m + n <= 200
        # -10^9 <= nums1[i], nums2[i] <= 10^9
        # nums1 and nums2 both are sorted in ascending order.
        # If nums1 is empty, return nums2.
        # If nums2 is empty, return nums1.

        # If nums1 is empty, return nums2.
        if not nums1:
            return nums2

        # If nums2 is empty, return nums1.
        if not nums2:
            return nums1

        # Loop over length of nums1.
        for i in range(len(nums1)):
            # If i is greater than or equal to m:
            if i >= m:
                # Set nums1[i] to nums2[i - m].
                nums1[i] = nums2[i - m]

        # Sort nums1.
        nums1.sort()

        # Return nums1.
        return nums1
        
