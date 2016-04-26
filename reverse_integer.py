class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        l = []

        s = abs(x)
        while s > 0:
        	l.append(s % 10)
        	s = s / 10

        r = 0
        for i in range(len(l)):
        	r += l[i] * pow(10, len(l) - i - 1)

        if x < 0:
        	r *= -1

        if r > 2147483647 or r < -2147483647:
        	return 0

        return r