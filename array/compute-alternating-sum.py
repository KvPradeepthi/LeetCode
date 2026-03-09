class Solution:
    def alternatingSum(self, nums):
        total = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                total += nums[i]   # even index → add
            else:
                total -= nums[i]   # odd index → subtract
        return total
