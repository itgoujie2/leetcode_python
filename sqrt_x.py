class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left = 1
        right = x
        
        while left < right:
            mid = left + (right - left) / 2 + 1
            
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid
                
        return left
            