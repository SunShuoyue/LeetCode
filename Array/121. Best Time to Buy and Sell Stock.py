class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        a = 0
        if len(prices) < 2:
            return 0
        ind = [i for i in range(1, len(prices)) if (prices[i] - prices[i - 1]) > 0]
        for i in range(len(ind)):
            for j in ind[i:]:
                d = prices[j] - prices[ind[i] - 1]
                if d > a:
                    a = d
        return a
