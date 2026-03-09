from typing import List
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = [0] * 101
        res = []

        def add(v):
            freq[v + 50] += 1

        def remove(v):
            freq[v + 50] -= 1

        for i in range(k):
            add(nums[i])

        for i in range(k, len(nums) + 1):
            cnt = 0
            beauty = 0
            for v in range(0, 50):
                cnt += freq[v]
                if cnt >= x:
                    beauty = v - 50
                    break
            res.append(beauty)

            if i == len(nums):
                break
            remove(nums[i - k])
            add(nums[i])

        return res
