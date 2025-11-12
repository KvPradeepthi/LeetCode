from math import gcd
from functools import reduce

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        
        # Step 1: If overall gcd != 1 → impossible
        overall_gcd = reduce(gcd, nums)
        if overall_gcd != 1:
            return -1
        
        # Step 2: If any element is already 1
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        # Step 3: Find smallest subarray whose gcd = 1
        min_len = float('inf')
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        # Step 4: total = (len_of_subarray - 1) + (n - 1)
        return (min_len - 1) + (n - 1)
