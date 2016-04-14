class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = sorted(nums)
        for i in range(len(temp) - 1):
        	if (temp[i] == temp[i+1]):
        		return True

        return False