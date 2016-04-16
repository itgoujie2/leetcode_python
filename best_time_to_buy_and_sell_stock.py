class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) == 0:
            return 0
        
        max = 0
        low = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            if prices[i] - low > max:
                max = prices[i] - low
                
        return max
        