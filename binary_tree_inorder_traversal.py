# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         if root == None:
#             return []
        
#         result = []
#         self.dfs(root, result)
        
#         return result
        
#     def dfs(self, root, result):
#         if root == None:
#             return
        
#         self.dfs(root.left, result)
#         result.append(root.val)
#         self.dfs(root.right, result)
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
            
        result = []
        cur = root
        tracker = []
        while cur != None or tracker:
            if cur != None:
                tracker.append(cur)
                cur = cur.left
            else:
                cur = tracker.pop()
                result.append(cur.val)
                cur = cur.right
        
        return result
        