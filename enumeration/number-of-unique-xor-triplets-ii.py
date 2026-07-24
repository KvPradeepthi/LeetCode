class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pair = set()
        for a in nums:
            for b in nums:
                pair.add(a ^ b)
        ans = set()
        for x in pair:
            for c in nums:
                ans.add(x ^ c)
        return len(ans)
        