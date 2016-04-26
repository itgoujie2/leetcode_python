class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 3 == 1:
            return 2 * 2 * pow(3, (n-4)/3)
        elif n % 3 == 2:
            return 2 * pow(3, (n-2)/3)
        else:
            return pow(3, n/3)