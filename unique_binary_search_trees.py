class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [0]*(n+1)
        return self.helper(n, cache)

    def helper(self, n, cache):
    	if n == 0 or n == 1:
    		return 1

    	if cache[n] > 0:
    		return cache[n]

    	k = 0
    	for i in xrange(1, n+1):
    		k += max(1, self.helper(i-1, cache)) * max(1, self.helper(n-i, cache))

    	cache[n] = k
        
        return k