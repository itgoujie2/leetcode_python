class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, m = len(nums1), len(nums2)
        ret = [0]*k
        
        for i in range(k+1):
            j = k - i
            if i > n or j > m:
                continue
            left = self.findMax(nums1, i)
            right = self.findMax(nums2, j)
            ret = max(self.merge(left, right), ret)
            
        return ret
        
    def merge(self, left, right):
        ans = []
        while left or right:
            if left > right:
                ans.append(left[0])
                left = left[1:]
            else:
                ans.append(right[0])
                right = right[1:]
        
        return ans
        
    def findMax(self, nums, selects):
        n = len(nums)
        ret = [-1]
        if selects > n:
            return ret
        while selects > 0:
            start = ret[-1] + 1
            end = n - selects + 1
            ret.append(max(range(start, end), key = nums.__getitem__))
            selects -= 1
        ret = [nums[item] for item in ret[1:]]
        
        return ret