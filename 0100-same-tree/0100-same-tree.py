# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # Given the roots of two binary trees p and q, write a function to check if they are the same or not.

        # Thoughts/constraints/edge cases:
        # The number of nodes in both trees is in the range [0, 100].
        # -10^4 <= Node.val <= 10^4
        # If both trees are empty, return True.
        # If one tree is empty and the other is not, return False.
        # If both trees are not empty, compare values of nodes.

        # If both trees are empty, return True.
        if p == None and q == None:
            return True

        # If one tree is empty and the other is not, return False.
        if p == None or q == None:
            return False

        # If both trees are not empty, compare values of nodes.
        # If values are not equal, return False.
        if p.val != q.val:
            return False

        # If values are equal, compare left and right subtrees.
        # If left subtrees are not equal, return False.
        if not self.isSameTree(p.left, q.left):
            return False

        # If right subtrees are not equal, return False.
        if not self.isSameTree(p.right, q.right):
            return False

        # If all subtrees are equal, return True.
        return True
        
