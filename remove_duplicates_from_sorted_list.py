# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        tracker = head
        while tracker != None:
            if tracker.next != None and tracker.val == tracker.next.val:
                tracker.next = tracker.next.next
            else:
                tracker = tracker.next
            
        return head
        