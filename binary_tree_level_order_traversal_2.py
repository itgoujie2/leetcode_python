# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        self.dfs([root], res)
        return res
        
    def dfs(self, level_nodes, res):
        if not level_nodes:
            return
        res.insert(0, [])
        temp = []
        for n in level_nodes:
            res[0].append(n.val)
            if n.left:
                temp.append(n.left)
            if n.right:
                temp.append(n.right)
        self.dfs(temp, res)