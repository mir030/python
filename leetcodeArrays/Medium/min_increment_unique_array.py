class Solution(object):
    def minIncrementForUnique(self, nums):
        count = 0
        for item in nums:
            if nums.count(item) > 1:
                item_index = nums.index(item)
                item = item + 1
                count += 1
                while item in nums:
                    item = item + 1
                    count += 1
                nums[item_index] = item
        return count


solution = Solution()
print(solution.minIncrementForUnique([2, 2, 2, 2, 0]))