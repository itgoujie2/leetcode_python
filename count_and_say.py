class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        pre = self.countAndSay(n -1)
        temp = ''
        tracker = 0
        while tracker < len(pre):
            num = 1
            while tracker < len(pre) - 1 and pre[tracker] == pre[tracker+1]:
                num += 1
                tracker += 1
            temp += str(num) + pre[tracker]
            tracker += 1
        
        return temp