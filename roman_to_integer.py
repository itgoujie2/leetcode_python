class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tracker = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        carry = 0
        previous = 4000
        for i in range(len(s)):
            val = tracker[s[i]]
            if previous > val:
                result += carry
                carry = val
            elif previous == val:
                carry += val
            else:
                carry = -carry + val
            previous = val
                
        return result + carry