class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)//2):
            a = nums.pop()
            if a in nums:
                nums.remove(a)
            else:
                return a
        return nums[0]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res^=i
        return res