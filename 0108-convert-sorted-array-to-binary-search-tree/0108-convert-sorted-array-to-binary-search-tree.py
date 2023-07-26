# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # Convert a sorted array to a height-balanced binary search tree.

        # Thoughts/constraints/edge cases:
        # The array is sorted, so we can use binary search to find the middle element
        # The middle element will be the root of the tree
        # The left half of the array will be the left subtree
        # The right half of the array will be the right subtree
        # 1 <= nums.length <= 10^4
        # -10^4 <= nums[i] <= 10^4
        # nums is sorted in a strictly increasing order.

        # Base case: if the array is empty, return None
        if not nums:
            return None

        # Find the middle element
        mid = len(nums) // 2

        # Create a node with the middle element as the value
        node = TreeNode(nums[mid])

        # Recursively call the function on the left half of the array
        node.left = self.sortedArrayToBST(nums[:mid])

        # Recursively call the function on the right half of the array
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        # Return the node
        return node



        
