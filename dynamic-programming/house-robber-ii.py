class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def rob(arr):
            p2=0
            p1=0
            for i in arr:
                cur=max(p1,p2+i)
                p2=p1
                p1=cur
            return p1
        return max(
            rob(nums[:-1]),
            rob(nums[1:])
        )


            