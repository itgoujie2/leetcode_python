class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        map = [ [1 for x in range(n)] for y in range(m) ]

        for i in range(1, m):
        	for j in range(1, n):
        		map[i][j] = map[i-1][j] + map[i][j-1]

        return map[-1][-1]