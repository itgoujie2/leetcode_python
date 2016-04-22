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
        if head == None:
        	return False

        slow = head
        fast = slow.next
        while fast != None:
        	if slow == fast:
        		return True
        	slow = slow.next
        	if fast.next != None:
        		fast = fast.next.next
        	else:
        		return False
        return False