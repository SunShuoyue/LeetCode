class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        exs = []
        while n != 1:
            if n in exs:
                return False
            exs.append(n)
            n = sum([int(i)**2 for i in list(str(n))])
        else:
            return True
