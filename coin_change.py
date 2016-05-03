class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [sys.maxint]*amount
        
        for cents in range(1, amount+1):
            dp[cents] = min([dp[cents - c] if cents - c >= 0 else sys.maxint for c in coins]) + 1
            
        return dp[amount] if dp[amount] < sys.maxint else -1