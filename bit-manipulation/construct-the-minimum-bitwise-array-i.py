class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n & (n - 1) == 0:
                ans.append(-1)
            else:
                temp = n
                count = 0
                while temp & 1:
                    count += 1
                    temp >>= 1
                ans.append(n - (1 << (count - 1)))
        return ans
