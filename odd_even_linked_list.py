# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
        	return None

        odd = head
        even = None
        if odd.next:
        	even = odd.next

        if not even:
        	return odd

        odd_start = odd
        even_start = even

        while odd.next or even.next:
        	if even:
        		odd.next = even.next
        	if odd.next:
        		even.next = odd.next.next

        	if odd.next:
        		odd = odd.next
        	if even.next:
        		even = even.next

        odd.next = even_start

        return odd_start


