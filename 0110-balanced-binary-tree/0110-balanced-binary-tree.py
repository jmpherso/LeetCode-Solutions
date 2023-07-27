# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Given a binary tree, determine if it is height-balanced.

        # Thoughts/constraints/edge cases:
        # A height-balanced binary tree is defined as:
        # a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
        # The number of nodes in the tree is in the range [0, 5000].
        # -10^4 <= Node.val <= 10^4
        # Note, cannot use self.height() because it is not a static method
        # Need to use self.isBalanced() recursively

        # Helper function to find the height of a tree
        def height(node):
            # Base case: if the node is None, return 0
            if not node:
                return 0

            # Recursively call the function on the left and right subtrees
            left = height(node.left)
            right = height(node.right)

            # Return the max of the left and right subtrees + 1
            return max(left, right) + 1

        # Base case: if the root is None, return True
        if not root:
            return True

        # Recursively call the function on the left and right subtrees
        left = height(root.left)
        right = height(root.right)

        # If the absolute difference between the left and right subtrees is greater than 1, return False
        if abs(left - right) > 1:
            return False

        # Recursively call the function on the left and right subtrees
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        # Return True if both subtrees are balanced
        return left and right

