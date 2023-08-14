# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.

        # Thoughts/constraints/edge cases:
        # The number of nodes of listA is m, the number of nodes of listB is n.
        # 0 <= m, n <= 3 * 10^4
        # 1 <= Node.val <= 10^5
        # 0 <= skipA <= m
        # 0 <= skipB <= n

        # Create two pointers, one for each list
        # Traverse each list until the end
        # If the pointers are equal, return the node
        # If the pointers are not equal, return None

        # Make pointers
        pointerA = headA
        pointerB = headB

        # Traverse lists
        while pointerA != pointerB:
            if pointerA:
                pointerA = pointerA.next
            else:
                pointerA = headB
            if pointerB:
                pointerB = pointerB.next
            else:
                pointerB = headA

        # Return node
        return pointerA
