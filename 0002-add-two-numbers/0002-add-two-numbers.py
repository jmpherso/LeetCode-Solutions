# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #Sum two linked lists, l1 and l2, and return the sum as a linked list

        #Create a new linked list to store the sum
        sum = ListNode()
        #Create a pointer to the head of the new linked list
        sum_pointer = sum
        #Create a carry variable to store the carry value
        carry = 0
        #While l1 or l2 or carry is not None
        while l1 or l2 or carry:
            #If l1 is not None
            if l1:
                #Add l1.val to carry
                carry += l1.val
                #Move l1 to the next node
                l1 = l1.next
            #If l2 is not None
            if l2:
                #Add l2.val to carry
                carry += l2.val
                #Move l2 to the next node
                l2 = l2.next
            #Add the carry value to the new linked list
            sum_pointer.next = ListNode(carry % 10)
            #If the carry value is greater than 9
            if carry > 9:
                #Set the carry value to 1
                carry = 1
            #Else
            else:
                #Set the carry value to 0
                carry = 0
            #Move the pointer to the next node
            sum_pointer = sum_pointer.next
        #Return the head of the new linked list
        return sum.next
