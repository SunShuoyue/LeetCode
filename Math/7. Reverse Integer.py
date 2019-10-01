class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            num = str(x)[1:]
            neg = True
        else:
            num = str(x)
            neg = False
        res = ''
        for i in reversed(num):
            res+=i
        if neg:
            res = '-' + res
            if int(res) < -2**31:
                return 0
        else:
            if int(res) > 2**31:
                return 0
        return int(res)


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        re_string = str(x)[::-1]
        if re_string[-1] == '-':
            re_string = re_string[-1]+re_string[0:-1]
        output = int(re_string)
        if output > 2**31 or output < -2**31:
            output = 0
        return(output)



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=cmp(x,0);r=int(`s*x`[::-1]);return(r<2**31)*s*r

