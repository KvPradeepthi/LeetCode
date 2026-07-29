class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        t=min(k,mul-1)
        ans=0
        for i in range(t):
            ans+=nums[i]*(mul-i)
        for i in range(t,k):
            ans+=nums[i]
        return ans
        