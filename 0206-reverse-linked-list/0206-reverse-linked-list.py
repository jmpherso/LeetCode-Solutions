class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Reverse a singly linked list.

        # Thoughts/constraints/edge cases:
        # 1 <= Node.val <= 50
        # 0 <= k <= 50

        # Approach 1: Iteration
        # Time: O(n) Space: O(1)

        # Create prev and curr
        prev, curr = None, head

        # Iterate through linked list
        while curr:
            # Create temp
            temp = curr.next
            # Set curr.next to prev
            curr.next = prev
            # Set prev to curr
            prev = curr
            # Set curr to temp
            curr = temp

        # Return prev
        return prev
        
# leetcode submit region end(Prohibit modification and deletion)
