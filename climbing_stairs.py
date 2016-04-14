# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         dp = [None]*1000
#         dp[0] = 1
#         dp[1] = 1
        
        
#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
        
#         return dp[n]
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(a, b, index):
            if (index == n):
                return b
            return helper(b, a+b, index+1)
            
        return helper(0, 1, 0)
        
        