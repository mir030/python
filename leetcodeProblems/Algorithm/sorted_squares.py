class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums


s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 2]))
