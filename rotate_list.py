# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
        	return None

        # find end
        p1 = head
        l = 1
        end = head
        while p1.next:
        	p1 = p1.next
        	if not p1.next:
        		end = p1
        	l += 1

        if (l - k % l) % l == 0:
        	return head

        k = (l - k % l) % l

        p2 = head
        while k > 1:
        	p2 = p2.next
        	k -= 1

        new_head = p2.next
        p2.next = None
        end.next = head

        return new_head