from typing import List
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        vals.append(grid[r][c])

                vals = sorted(set(vals))
                if len(vals) <= 1:
                    ans[i][j] = 0
                else:
                    diff = float('inf')
                    for x in range(1, len(vals)):
                        diff = min(diff, vals[x] - vals[x - 1])
                    ans[i][j] = diff

        return ans
