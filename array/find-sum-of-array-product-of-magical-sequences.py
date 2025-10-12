from functools import lru_cache

MOD = 10**9 + 7

def magicalSum(m, k, nums):
    n = len(nums)
    
    @lru_cache(None)
    def dfs(rem, val):
        if rem == 0:
            return 1 if bin(val).count('1') == k else 0
        total = 0
        for i in range(n):
            total += dfs(rem - 1, val + (1 << i))
        return total
    
    @lru_cache(None)
    def dfs_prod(rem, val):
        if rem == 0:
            return 1 if bin(val).count('1') == k else 0
        total = 0
        for i in range(n):
            total += nums[i] * dfs_prod(rem - 1, val + (1 << i))
        return total % MOD

    return dfs_prod(m, 0) % MOD
