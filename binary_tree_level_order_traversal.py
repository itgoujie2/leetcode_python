# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        self.bfs([root], res)
        return res
    def bfs(self, level_nodes, res):
        if not level_nodes:
            return 
        
        temp = []
        level_temp = []
        for n in level_nodes:
            temp.append(n.val)
            if n.left != None:
                level_temp.append(n.left)
            if n.right != None:
                level_temp.append(n.right)
        res.append(temp)
        self.bfs(level_temp, res)