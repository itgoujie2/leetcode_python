class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return 0
        
        rob_prev = 0
        no_rob_prev = 0
        for n in nums:
            no_rob_cur = max(rob_prev, no_rob_prev)
            rob_cur = n + no_rob_prev
            
            rob_prev = rob_cur
            no_rob_prev = no_rob_cur
            
        return max(rob_prev, no_rob_prev)