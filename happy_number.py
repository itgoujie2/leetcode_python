class Solution(object):
    visited = set([])
    # def __init__(self):
    #     self.visited = set([])
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print('visited', self.visited)
        sum = 0
        for c in str(n):
            sum += int(c) * int(c)
        if sum == 1:
            return True
        if sum in self.visited:
            return False
        else:
            self.visited.add(n)
            self.visited.add(sum)
            return self.isHappy(sum)
                