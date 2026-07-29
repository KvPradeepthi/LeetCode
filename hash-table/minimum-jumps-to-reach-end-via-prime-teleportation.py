from collections import defaultdict, deque
from math import isqrt
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return True
        mp = defaultdict(list)
        for i, val in enumerate(nums):
            temp = val
            factors = set()
            d = 2
            while d * d <= temp:
                while temp % d == 0:
                    factors.add(d)
                    temp //= d
                d += 1
            if temp > 1:
                factors.add(temp)
            for f in factors:
                mp[f].append(i)
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        used_prime = set()
        jumps = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n - 1:
                    return jumps
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)
                val = nums[i]
                if is_prime(val) and val not in used_prime:
                    for nxt in mp[val]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)
                    used_prime.add(val)
            jumps += 1
        return -1