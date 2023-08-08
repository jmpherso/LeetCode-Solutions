# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Given head, the head of a linked list, determine if the linked list has a cycle in it.

        # Thoughts/constraints/edge cases:
        # head is a ListNode
        # 0 <= Node.val <= 10^5
        # pos is -1 or a valid index in the linked-list.
        # pos is -1 if there is no cycle in the linked list.
        # list can have 0 nodes

        # Base case, head is None
        if head is None:
            return False

        # Create a set to store the nodes we've seen
        seen = set()

        # Iterate through the linked list
        while head is not None:
            # If we've seen the current node before, return True
            if head in seen:
                return True

            # Add the current node to the set
            seen.add(head)

            # Move to the next node
            head = head.next

        # If we get to the end of the linked list, return False
        return False
