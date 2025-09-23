class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxc=cur=nums[0]
        for i in range(1,len(nums)):
            cur=max(nums[i],cur+nums[i])
            maxc=max(maxc,cur)
        return maxc
    
        