# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # Given the root of a binary tree, return the inorder traversal of its nodes' values.

        # Thoughts/constraints/edge cases:
        # The number of nodes in the tree is in the range [0, 100].
        # -100 <= Node.val <= 100
        # Follow up: Recursive solution is trivial, could you do it iteratively?

        # Create list for storing values.
        values = []

        # Create recursive function for traversing tree.
        def traverse_tree(node):
            # If node is not None:
            if node != None:
                # Traverse left.
                traverse_tree(node.left)

                # Append node val to values.
                values.append(node.val)

                # Traverse right.
                traverse_tree(node.right)

        # Call recursive function on root.
        traverse_tree(root)

        # Return values.
        return values
    
        
