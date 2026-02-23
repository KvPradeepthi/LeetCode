class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Store prefix products in answer
        prefix = 1
        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]
        
        # Step 2: Multiply with suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer