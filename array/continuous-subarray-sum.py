class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        sum=0
        for i in range(0,n):
            sum+=nums[i]
            if sum==0:
                return True
                break
            if sum%k==0:
                return True
                break
        return False
          
        