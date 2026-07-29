class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        dravonikel = nums
        prev = 0
        ans = 0
        for i in range(n - 1):
            cur = max(0, prev + nums[i] - nums[i + 1])
            if cur > prev:
                ans += cur - prev
            prev = cur
        return ans
        