# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        
        head = ListNode
        tracker = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                tracker.next = l1
                l1 = l1.next
            else:
                tracker.next = l2
                l2 = l2.next
            tracker = tracker.next
        
        while l1 != None:
            tracker.next = l1
            tracker = tracker.next
            l1 = l1.next
        
        while l2 != None:
            tracker.next = l2
            tracker = tracker.next
            l2 = l2.next
            
        return head.next
        
        
        
        