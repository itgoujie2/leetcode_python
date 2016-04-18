class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        if nums:
            
            d = {}
            for i in range(len(nums)):
                if not nums[i] in d:
                    d[nums[i]] = i
                else:
                    if i - d[nums[i]] <= k:
                        return True
                    else:
                        d[nums[i]] = i
        
        return False
        