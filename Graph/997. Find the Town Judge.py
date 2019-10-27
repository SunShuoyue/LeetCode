class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if trust == []:
            if N == 1:
                return 1
            else:
                return -1
        if len(trust) == 1:
            return trust[0][1]
        unzip = list(zip(*trust))
        res = set(unzip[1]) - set(unzip[0])
        if len(res) == 1:
            city = set(range(1, N + 1)) - set([i[0] for i in trust if i[1] == sum(res)])
            if res == city:
                return list(res)[0]
            else:
                return -1
        else:
            return -1
