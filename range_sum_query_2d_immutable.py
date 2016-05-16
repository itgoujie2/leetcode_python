class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix == None or len(matrix) == 0:
            return None
        
        self.x = len(matrix)
        self.y = len(matrix[0])
        self.sum = [ [0 for i in range(self.y+1)] for j in range(self.x+1) ]
        self.sum[1][1] = matrix[0][0]
        
        for i in range(1, self.x+1):
            self.sum[i][1] = self.sum[i-1][1] + matrix[i-1][0]
            
        for j in  range(1, self.y+1):
            self.sum[1][j] = self.sum[1][j-1] + matrix[0][j-1]
            
        for i in range(2, self.x+1):
            for j in range(2, self.y+1):
                self.sum[i][j] = self.sum[i-1][j] + self.sum[i][j-1] - self.sum[i-1][j-1] + matrix[i-1][j-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum[row2+1][col2+1] - self.sum[row1][col2+1] - self.sum[row2+1][col1] + self.sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)