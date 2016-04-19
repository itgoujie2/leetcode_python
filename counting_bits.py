# class Solution(object):
#     def countBits(self, num):
#         """
#         :type num: int
#         :rtype: List[int]
#         """
#         result = []
#         for i in range(num+1):
#             result.append(str(bin(i)).count('1'))
            
#         return result

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r = []
        if num >= 0:
            r.append(0)
        
        for i in range(1, num+1):
            temp = r[i/2]
            if i % 2 == 1:
                temp += 1
            r.append(temp)
        
        return r