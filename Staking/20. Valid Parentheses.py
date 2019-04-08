class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check=[]
        pairs = {')':'(','}':'{',']':'['}
        for i in s:
            if i in pairs:
                if len(check)<1:
                    return False
                if check.pop() != pairs[i]:
                    return False
            else:
                check.append(i)
        if check == []:
            return True
        else:
            return False

