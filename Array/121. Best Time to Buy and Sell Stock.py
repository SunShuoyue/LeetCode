class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        a = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                d = prices[j] - prices[i]
                if d > a:
                    a = d
        return a
