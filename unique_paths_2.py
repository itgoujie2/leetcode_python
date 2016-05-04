class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        map = [ [0]*n for y in range(m) ]

        for i in range(m):
        	if obstacleGrid[i][0] == 1: 
        		break
        	map[i][0] = 1

        for j in range(n):
        	if obstacleGrid[0][j] == 1:
        		break
        	map[0][j] = 1

        for i in range(1, m):
        	for j in range(1, n):
        		if not obstacleGrid[i][j]:
        			map[i][j] = map[i-1][j] + map[i][j-1]

        return map[-1][-1]
