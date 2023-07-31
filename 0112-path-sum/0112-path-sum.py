# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        # Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

        # Thoughts/constraints/edge cases:
        # A leaf is a node with no children.
        # The number of nodes in the tree is in the range [0, 5000].
        # -1000 <= Node.val <= 1000
        # -1000 <= targetSum <= 1000

        # Base case: if the root is None, return False
        if not root:
            return False

        # If the root has no children, check if the root's value is equal to the targetSum
        if not root.left and not root.right:
            return root.val == targetSum

        # If the root has a left child, recursively call the function on the left subtree
        if root.left:
            left = self.hasPathSum(root.left, targetSum - root.val)

        # If the root has a right child, recursively call the function on the right subtree
        if root.right:
            right = self.hasPathSum(root.right, targetSum - root.val)

        # If the root has both a left and right child, return the left or right subtree
        if root.left and root.right:
            return left or right

        # If the root has only a left child, return the left subtree
        if root.left:
            return left

        # If the root has only a right child, return the right subtree
        if root.right:
            return right

        
        
