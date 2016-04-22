# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(t1, t2):
            if t1 == None and t2 == None:
                return True
            if t1 == None or t2 == None:
                return False
            return t1.val == t2.val and check(t1.left, t2.right) and check(t1.right, t2.left)
        
        
        if root == None:
            return True
        return check(root.left, root.right)