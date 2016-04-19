# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution(object):
#     def preorderTraversal(self, root):
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
#         result.append(root.val)
#         self.dfs(root.left, result)
#         self.dfs(root.right, result)
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
            
        result = []
        cur = root
        tracker = [cur]
        
        while tracker:
            cur = tracker.pop()
            if cur != None:
                result.append(cur.val)
                if cur.right != None:
                    tracker.append(cur.right)
                if cur.left != None:
                    tracker.append(cur.left)
        
        return result
                
                
                