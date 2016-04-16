class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        temp = []
        for i in xrange(len(self.s)):
            temp.append(self.s.pop())
        self.s.append(x)
        for j in xrange(len(temp)):
            self.s.append(temp.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        return self.s.pop()

    def peek(self):
        """
        :rtype: int
        """
        result = self.s.pop()
        self.s.append(result)
        return result

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s
        