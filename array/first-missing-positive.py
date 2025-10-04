class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: Replace non-positive numbers and numbers > n with a placeholder (n+1)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Mark presence by making index negative
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # Step 3: First index with a positive value means missing number
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # Step 4: If all numbers 1..n are present, answer is n+1
        return n + 1
