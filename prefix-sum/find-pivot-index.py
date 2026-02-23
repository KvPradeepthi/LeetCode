class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        lst1=[0]*n 
        lst3=[0]*n
        sum=0
        for i in range(0,n):
            sum=sum+nums[i]
            lst1[i]=sum
        sum=0
        for i in range(n-1,-1,-1):
            sum=sum+nums[i]
            lst3[i]=sum
        for i in range(0,n):
            if lst1[i]==lst3[i]:
                return i 
        else:
            return -1
        