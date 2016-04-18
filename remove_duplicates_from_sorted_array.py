class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0 if not nums else 1
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                nums.pop(slow)
            else:
                slow += 1
                fast += 1
        return len(nums)