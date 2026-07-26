class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        max_sum=float("-inf")
        for num in range(len(nums)):
            current_sum=max(current_sum+nums[num],nums[num])
            max_sum=max(max_sum,current_sum)
        return max_sum


            
