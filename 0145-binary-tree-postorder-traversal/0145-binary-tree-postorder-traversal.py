# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # Given the root of a binary tree, return the postorder traversal of its nodes' values.

        # Thoughts/constraints/edge cases:
        # The number of nodes in the tree is in the range [0, 100].
        # -100 <= Node.val <= 100
        # Follow up: Recursive solution is trivial, could you do it iteratively?
        # Postorder traversal: left, right, root

        # Base case
        if not root:
            return []

        # Recursive case
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
