# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
        	return []

        tracker = []
        result = []
        tracker.append((root, False))

        while tracker:
        	node, visited = tracker.pop()
        	if node:
        		if visited:
        			result.append(node.val)
        		else:
        			tracker.append((node, True))
        			tracker.append((node.right, False))
        			tracker.append((node.left, False))

        return result
