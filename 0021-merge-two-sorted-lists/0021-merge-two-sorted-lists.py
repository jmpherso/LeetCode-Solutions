# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Merge two sorted linked list into one sorted linked list.
        # Return head of sorted merged list.

        # Thoughts/constraints/edges :
        # List 1 and 2 are sorted ascending
        # List 1 and 2 can be empty - if both are empty, return empty list, if one is empty, return the other list

        # If list 1 is empty, return list 2
        if not list1:
            return list2

        # If list 2 is empty, return list 1
        if not list2:
            return list1

        # Create a new linked list to store the merged list
        merged_list = ListNode()

        # Create a pointer to the head of the merged list
        merged_list_pointer = merged_list

        # While list 1 and list 2 are not empty
        while list1 and list2:
            # If the value of list 1 is less than or equal to the value of list 2
            if list1.val <= list2.val:
                # Set the next node of the merged list to list 1
                merged_list_pointer.next = list1
                # Move list 1 to the next node
                list1 = list1.next
            # Else
            else:
                # Set the next node of the merged list to list 2
                merged_list_pointer.next = list2
                # Move list 2 to the next node
                list2 = list2.next
            # Move the pointer to the next node
            merged_list_pointer = merged_list_pointer.next

        # If list 1 is not empty
        if list1:
            # Set the next node of the merged list to list 1
            merged_list_pointer.next = list1
        # Else
        else:
            # Set the next node of the merged list to list 2
            merged_list_pointer.next = list2

        # Return the head of the merged list
        return merged_list.next

