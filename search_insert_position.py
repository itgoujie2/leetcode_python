# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if not nums:
#             return 0
        
#         nums.insert(0, -sys.maxint)
#         nums.append(sys.maxint)
        
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i-1
#             elif target > nums[i] and target < nums[i+1]:
#                 return i
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, mid = 0, 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) / 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
                
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
        