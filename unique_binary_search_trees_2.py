class Solution(object):
        def generateTrees(self, n):
            """
            :type n: int
            :rtype: List[TreeNode]
            """
            if n == 0:
                return []
            return self.helper(range(1, n+1))

        def helper(self, num):
            if len(num) == 0:
            	return [None]
            elif len(num) == 1:
            	return [TreeNode(num[0])]
            else:
            	result = []
            	for i, val in enumerate(num):
            		left = self.helper(num[:i])
            		right = self.helper(num[i+1:])

            		for l in left:
            			for r in right:
            				root = TreeNode(val)
            				root.left = l
            				root.right = r
            				result.append(root)

            	return result