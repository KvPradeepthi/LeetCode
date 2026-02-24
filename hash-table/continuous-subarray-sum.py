class Solution:
    def checkSubarraySum(self, nums, k):
        n=len(nums)
        rem_map={0:-1}
        p_sum=0
        for i in range(0,n):
            p_sum+=nums[i]
            rem=p_sum%k
            if rem in rem_map:
                if i-rem_map[rem]>1:
                    return True
            else:
                rem_map[rem]=i
        return False