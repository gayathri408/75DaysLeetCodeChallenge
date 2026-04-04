class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        for i in range(n):
            if target <= nums[i]:
                return i
        return n