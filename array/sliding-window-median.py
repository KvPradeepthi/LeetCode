import heapq
from collections import defaultdict
from typing import List
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small, large = [], []
        delayed = defaultdict(int)
        res = []
        small_size = large_size = 0

        def prune_small():
            while small and delayed[-small[0]] > 0:
                delayed[-small[0]] -= 1
                heapq.heappop(small)

        def prune_large():
            while large and delayed[large[0]] > 0:
                delayed[large[0]] -= 1
                heapq.heappop(large)

        def balance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                val = -heapq.heappop(small)
                small_size -= 1
                heapq.heappush(large, val)
                large_size += 1
                prune_small()
            elif small_size < large_size:
                val = heapq.heappop(large)
                large_size -= 1
                heapq.heappush(small, -val)
                small_size += 1
                prune_large()

        for i, num in enumerate(nums):
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1

            balance()

            if i >= k:
                out = nums[i - k]
                delayed[out] += 1
                if out <= -small[0]:
                    small_size -= 1
                    if out == -small[0]:
                        prune_small()
                else:
                    large_size -= 1
                    if large and out == large[0]:
                        prune_large()
                balance()

            if i >= k - 1:
                if k % 2:
                    res.append(float(-small[0]))
                else:
                    res.append(((-small[0]) + large[0]) / 2.0)

        return res
