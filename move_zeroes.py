# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         tracker = 0
#         while tracker < len(nums):
#             if nums[tracker] == 0:
#                 mover = tracker + 1
                
#                 while mover<len(nums) and nums[mover] == 0:
#                     mover += 1
                    
#                 if mover < len(nums):
#                     temp = nums[mover]
#                     nums[mover] = nums[tracker]
#                     nums[tracker] = temp
                
#             tracker += 1
            
#         

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         for i in nums:
#             if i == 0:
#                 nums.remove(0)
#                 nums.append(0)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = 0
        for l in range(len(nums)):
            if nums[l] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                r += 1
                