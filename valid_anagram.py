class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(t) > len(s)):
            long = t
            short = s
        else:
            long = s
            short = t
        
        tracker = {}
        for z in range(97, 123):
            tracker[chr(z)] = 0
        for j in range(len(long)):
            tracker[long[j]] += 1
            
        for i in range(len(short)):
            tracker[short[i]] -= 1
            
        for k in range(97, 123):
            if tracker[chr(k)] > 0:
                return False
        
        return True