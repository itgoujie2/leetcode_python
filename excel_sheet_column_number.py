class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
        	temp = ord(s[i]) - 64
        	sum += temp * pow(26, len(s)-i-1)
        return sum