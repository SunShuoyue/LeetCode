class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = [-1] * len(nums1)
        s = []
        for num in nums2:
            while s:
                if num > s[-1]:
                    nums[nums1.index(s.pop())] = num
                else:
                    break
            if num in nums1:
                s.append(num)
        return nums
