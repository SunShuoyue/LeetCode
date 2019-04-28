class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(digits)+1):
            if digits[-i] == 9:
                digits[-i] = 0
                continue
            else:
                digits[-i] += 1
                return digits
        digits.insert(0,1)
        return digits
