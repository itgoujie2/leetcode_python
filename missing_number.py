class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        
        for i in range(1, len(nums)+1):
        	sum1 += i

        

        return sum1 - sum(nums)