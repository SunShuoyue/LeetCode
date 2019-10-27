class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        if len(nums) == 2:
            if len(set(nums)) == 1:
                nums.remove(nums[0])
                return len(nums)
            else:
                return len(nums)
        lenth = len(set(nums))
        i = 1
        while i < lenth:
            if nums[-i] == nums[-i - 1]:
                nums.remove(nums[-i])
            else:
                i += 1
        while len(nums) > lenth:
            nums.remove(nums[0])
        return len(nums)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = self.removeD(nums)
        return len(nums)

    def removeD(self, nums):
        if len(nums) <= 1:
            return nums
        if nums[0] == nums[-1]:
            nums[:] = nums[:1]
            return nums
        mid = nums[len(nums) // 2]
        if mid == nums[len(nums) // 2 - 1]:
            nums = self.removeD(nums[:len(nums) // 2]) + self.removeD(nums[len(nums) // 2:])
            nums.remove(mid)
            return nums
        else:
            nums = self.removeD(nums[:len(nums) // 2]) + self.removeD(nums[len(nums) // 2:])
            return nums


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = self.removeD(nums)
        return len(nums)

    def removeD(self, nums):
        if len(nums) <= 1:
            return nums
        if nums[0] == nums[-1]:
            nums[:] = nums[:1]
            return nums
        if len(nums) == 2:
            return nums
        nums = self.removeD(nums[:len(nums) // 2 + 1])[:-1] + self.removeD(nums[len(nums) // 2:])
        return nums


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
