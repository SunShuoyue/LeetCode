class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while nums:
            try:
                nums.remove(val)
            except:
                return len(nums)
        return 0
