# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

        # Thoughts/constraints/edge cases:
        # 0 <= num of nodes <= 300
        # -100 <= Node.val <= 100
        # The list is guaranteed to be sorted in ascending order.
        # If num of nodes is 0, return None.
        # If num of nodes is 1, return head.

        # If num of nodes is 0, return None.
        if head == None:
            return None

        # If num of nodes is 1, return head.
        if head.next == None:
            return head

        # Create pointer for current node.
        current_node = head

        # Create pointer for next node.
        next_node = head.next

        # While next node is not None:
        while next_node != None:
            # If current node val is equal to next node val:
            if current_node.val == next_node.val:
                # Set current node next to next node next.
                current_node.next = next_node.next

                # Set next node to current node next.
                next_node = current_node.next
            else:
                # Set current node to next node.
                current_node = next_node

                # Set next node to current node next.
                next_node = current_node.next

        # Return head.
        return head
        
