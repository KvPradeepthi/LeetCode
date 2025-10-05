from typing import List
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        min_sum1 = sum1 + zeros1
        min_sum2 = sum2 + zeros2
        max_sum1 = sum1 + zeros1 * 10**6
        max_sum2 = sum2 + zeros2 * 10**6
        if min_sum1 > max_sum2 or min_sum2 > max_sum1:
            return -1
        return max(min_sum1, min_sum2)
