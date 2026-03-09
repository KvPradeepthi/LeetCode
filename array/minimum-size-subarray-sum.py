class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        c=0
        minsum=float('inf')
        for right in range(len(nums)):
            c=c+nums[right]
            while c>=target:
                minsum=min(minsum,right-left+1)
                c=c-nums[left]
                left=left+1
        if minsum==float('inf'):
            return 0
        else:
            return minsum
        
        