class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = ans = nums[0]
        for num in nums[1:]:
            temp_max = max(num, cur_max * num, cur_min * num)
            cur_min = min(num, cur_max * num, cur_min * num)
            cur_max = temp_max
            ans = max(ans, cur_max)
        return ans