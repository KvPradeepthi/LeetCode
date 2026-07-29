from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        right = sum(nums)
        left = 0
        for i in range(n):
            right -= nums[i]
            ans[i] = abs(left - right)
            left += nums[i]
        return ans