class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in set(nums):
        	if nums.count(n) > len(nums)/2:
        		return n