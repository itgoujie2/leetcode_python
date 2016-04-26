# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        # find the mid
        while fast and fast.next:
        	slow = slow.next
        	fast = fast.next.next

        # reverse the second half
        node = None
        while slow:
        	nxt = slow.next
        	slow.next = node
        	node = slow
        	slow = nxt

        while node:
        	if head.val != node.val:
        		return False

        	head = head.next
        	node = node.next

        return True