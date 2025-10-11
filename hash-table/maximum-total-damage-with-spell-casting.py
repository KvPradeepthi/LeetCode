from collections import Counter
from bisect import bisect_left
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        nums = sorted(freq.keys())
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0] * freq[nums[0]]
        
        for i in range(1, n):
            total = nums[i] * freq[nums[i]]
            j = bisect_left(nums, nums[i] - 2) - 1
            
            if j >= 0:
                total += dp[j]
            
            dp[i] = max(dp[i-1], total)
        
        return dp[-1]
