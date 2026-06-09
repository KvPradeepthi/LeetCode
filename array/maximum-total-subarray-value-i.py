class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maximum = nums[0]
        minimum = nums[0]
        for num in nums:
            if num > maximum:
                maximum = num
            if num < minimum:
                minimum = num
        return k * (maximum - minimum)