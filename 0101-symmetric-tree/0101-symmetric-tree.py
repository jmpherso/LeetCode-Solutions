# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

        # Thoughts/constraints/edge cases:
        # The number of nodes in the tree is in the range [1, 1000].
        # -100 <= Node.val <= 100
        # Follow up: Could you solve it both recursively and iteratively?

        # Create recursive function for checking if tree is symmetric.
        def is_symmetric(left, right):
            # If left and right are both None, return True.
            if left == None and right == None:
                return True

            # If left and right are not both None, check if values are equal.
            if left != None and right != None:
                # If values are equal, check if subtrees are symmetric.
                if left.val == right.val:
                    # If subtrees are symmetric, return True.
                    if is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left):
                        return True

            # If values are not equal or subtrees are not symmetric, return False.
            return False

        # Call recursive function on root.
        return is_symmetric(root.left, root.right)
