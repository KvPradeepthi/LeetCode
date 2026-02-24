class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        sum=[0]*n
        for i in range(0,n):
            sum[i]+=sum[i-1]+nums[i]
            if sum[i]==0:
                return True
                break
            if sum[i]%k==0:
                return True
                break
        return False
          
        