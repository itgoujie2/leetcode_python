class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
        	return 0

        # forward
        forward = [0]*len(prices)
        min_buy = prices[0]
        for i in range(1, len(prices)):
        	forward[i] = max(forward[i-1], prices[i] - min_buy)
        	min_buy = min(min_buy, prices[i])

        # backward
        backward = [0]*len(prices)
        max_sell = prices[len(prices)-1]
        for j in range(len(prices)-2, -1, -1):
        	backward[j] = max(backward[j+1], max_sell - prices[j])
        	max_sell = max(max_sell, prices[j])

        result = 0
        for k in range(len(prices)):
        	result = max(result, forward[k] + backward[k])

        return result