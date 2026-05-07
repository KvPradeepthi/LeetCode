class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                three=a+nums[l]+nums[r]
                if three>0:
                    r=r-1
                elif three<0:
                    l=l+1
                else:
                    res.append([a,nums[l],nums[r]])
                    l=l+1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
        return res
            