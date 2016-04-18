class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        total = m + n - 1
        m -= 1
        n -= 1
        
        
        while total >= 0:
            if m >= 0 and (n < 0 or nums1[m] > nums2[n]):
                nums1[total] = nums1[m]
                m -= 1
            else:
                nums1[total] = nums2[n]
                n -= 1
            total -= 1
            