# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # Given a binary tree, find its minimum depth.

        # Thoughts/constraints/edge cases:
        # The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
        # A leaf is a node with no children.
        # The number of nodes in the tree is in the range [0, 10^5].
        # -1000 <= Node.val <= 1000

        # Base case: if the root is None, return 0
        if not root:
            return 0

        # If the root has no children, return 1
        if not root.left and not root.right:
            return 1

        # If the root has a left child, recursively call the function on the left subtree
        if root.left:
            left = self.minDepth(root.left)

        # If the root has a right child, recursively call the function on the right subtree
        if root.right:
            right = self.minDepth(root.right)

        # If the root has both a left and right child, return the min of the left and right subtrees + 1
        if root.left and root.right:
            return min(left, right) + 1

        # If the root has only a left child, return the left subtree + 1
        if root.left:
            return left + 1

        # If the root has only a right child, return the right subtree + 1
        if root.right:
            return right + 1

