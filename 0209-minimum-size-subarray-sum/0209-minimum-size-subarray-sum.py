class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        current_sum=0
        minlen=float("inf")
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>=target:
                length=right-left+1
                minlen=min(length,minlen)
                current_sum-=nums[left]
                left+=1
        if minlen==float("inf"):
            return 0
        return minlen
        