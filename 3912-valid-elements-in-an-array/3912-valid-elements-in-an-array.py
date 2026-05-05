class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[]
        for i in range(n):
            if i==0 or i==n-1:
                res.append(nums[i])
                continue
            ele=True
            el=True
            for j in range(0,i):
                if nums[i]<=nums[j]:
                    ele=False
                    break
            for j in range(i+1,n):
                if nums[i]<=nums[j]:
                    el=False
                    break
            if ele or el:
                res.append(nums[i])
        return res
                    