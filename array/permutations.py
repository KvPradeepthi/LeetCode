class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return res
