class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []
        self.helper(0, 0, '', result, n)
        return result

    def helper(self, num_left, num_right, temp, result, n):
    	if num_left == n and num_right == n:
    		result.append(temp)
    		return

    	if num_left < n:
    		temp += '('
    		num_left += 1
    		self.helper(num_left, num_right, temp, result, n)
    		temp = temp[:-1]
    		num_left -= 1
    	if num_right < n and num_right < num_left:
    		temp += ')'
    		num_right += 1
    		self.helper(num_left, num_right, temp, result, n)
    		temp = temp[:-1]
    		num_right -= 1
