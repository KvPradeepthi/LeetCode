class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        p2=0
        p1=0
        for i in range(0,n):
            cur=max(p1,p2+nums[i])
            p2=p1
            p1=cur
        return p1
