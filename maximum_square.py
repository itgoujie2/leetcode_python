class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or len(matrix) == 0:
            return 0 
        
        x = len(matrix)
        y = len(matrix[0])
        dp = [ [0 for i in range(y)] for j in range(x)]
        
        for i in range(x):
            dp[i][0] = int(matrix[i][0])
            
        for j in range(y):
            dp[0][j] = int(matrix[0][j])
            
        for i in range(1, x):
            for j in range(1, y):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(int(dp[i-1][j]), int(dp[i][j-1]), int(dp[i-1][j-1])) + 1
                    
        ans = max( max(i) for i in dp )
        
        return ans * ans
                    
        