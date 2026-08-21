class Solution:
    def findKthSmallest(self, coins, k):
        from math import gcd
        n = len(coins)
        def lcm(a, b):
            return a // gcd(a, b) * b
        def count(x):
            total = 0
            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0
                valid = True
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])
                        if current_lcm > x:
                            valid = False
                            break
                if valid:
                    if bits % 2:
                        total += x // current_lcm
                    else:
                        total -= x // current_lcm
            return total
        left = 1
        right = min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left