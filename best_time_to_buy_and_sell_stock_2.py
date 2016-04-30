class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
            
        left = right = prices[0]
        
        sum = 0
        
        for next in prices[1:]:
            if next > right:
                right = next
            else:
                sum += (right - left)
                left = right = next
        
        
        sum += (right - left)
            
        return sum