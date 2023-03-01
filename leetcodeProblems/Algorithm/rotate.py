class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k - n
        nums[:] = nums[n-k:] + nums[0:n-k]
        return nums


s = Solution()
print(s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
