class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # Remove all elements from a linked list of integers that have value val.

        # Thoughts/constraints/edge cases:
        # 1 <= Node.val <= 50
        # 0 <= k <= 50

        # Approach 1: Iteration
        # Time: O(n) Space: O(1)

        # Create dummy node
        dummy = ListNode()

        # Set dummy.next to head
        dummy.next = head

        # Create prev and curr
        prev, curr = dummy, head

        # Iterate through linked list
        while curr:
            # If curr.val is val
            if curr.val == val:
                # Set prev.next to curr.next
                prev.next = curr.next
            # Else
            else:
                # Set prev to curr
                prev = curr
            # Set curr to curr.next
            curr = curr.next

        # Return dummy.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
