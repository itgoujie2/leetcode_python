# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return head

        tracker = head
        newHead = head
        while tracker.next != None:

        	temp = ListNode(tracker.next.val)
        	temp.next = newHead

        	newHead = temp
        	tracker = tracker.next

        head.next = None

        return newHead