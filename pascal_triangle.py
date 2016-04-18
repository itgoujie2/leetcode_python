# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         if numRows == 0:
#             return []
#         if numRows == 1:
#             return [[1]]
#         map = [[0 for x in range(numRows)] for x in range(numRows)]
#         for i in range(numRows):
#             temp = []
#             for j in range(i + 1):
#                 if j == 0 or j == i:
#                     temp.append(1)
#                 else:
#                     temp.append(map[i-1][j-1] + map[i-1][j])
#             map[i] = temp
#         return map
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1] * (i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        
        return result