# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []
        if root == None:
            return result
        self.dfs(root, '', result)
        return result
        
    def dfs(self, root, temp, result):
        if root == None:
            return
        temp = temp + str(root.val)
        if root.left != None:
            temp = temp + '->'
            self.dfs(root.left, temp, result)
            ri = temp.rfind('->')
            temp = temp[:ri]
        if root.right != None:
            temp = temp + '->'
            self.dfs(root.right, temp, result)
            ri = temp.rfind('->')
            temp = temp[:ri]
        if root.left == None and root.right == None:
            result.append(temp)
            return