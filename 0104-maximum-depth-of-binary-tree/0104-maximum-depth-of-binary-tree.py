# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Given the root of a binary tree, return its maximum depth.

        # Thoughts/constraints/edge cases:
        # The number of nodes in the tree is in the range [0, 10^4].
        # -100 <= Node.val <= 100
        # If tree is empty, return 0.
        # If tree is not empty, return max depth.

        # If tree is empty, return 0.
        if root == None:
            return 0

        # If tree is not empty, return max depth.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
