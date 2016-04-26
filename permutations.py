class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, [], result)
        return result

    def helper(self, nums, path, result):
    	if not nums:
    		result.append(path)

    	for i in range(len(nums)):
    		path.append([nums[i]])
    		self.helper(nums[:i] + nums[i+1:], path, result)