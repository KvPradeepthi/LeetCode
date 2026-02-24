class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        p=1
        for i in range(0,n):
            p*=nums[i]
            if p%k==0:
                return True
                break
        return False
          
        