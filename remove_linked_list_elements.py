# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        prev = ListNode(0)
        newHead = prev
        prev.next = head
        curr = head
        while curr != None:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
                
        return newHead.next