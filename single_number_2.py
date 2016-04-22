class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mySet = set(nums)
        mySum = sum(mySet)
        mySum *= 3
        return (mySum - sum(nums)) / 2