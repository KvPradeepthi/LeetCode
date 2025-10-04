class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        n = len(nums)
        
        for i, jump in enumerate(nums):
            if i > max_reach:
                # We can't reach this index
                return False
            # Update the farthest index we can reach
            max_reach = max(max_reach, i + jump)
        
        return max_reach >= n - 1

