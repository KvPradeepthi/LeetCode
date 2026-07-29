class Solution:
    def minElement(self, nums):
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        ans = float('inf')

        for num in nums:
            ans = min(ans, digit_sum(num))

        return ans