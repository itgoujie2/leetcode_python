class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*len(nums)
            
        for i in range(1, len(nums)):
            dp[i] = max( [dp[j] for j in range(i-1, -1, -1) if nums[i] > nums[j]] or [0] ) + 1
                    
        return max(dp or [0])
            