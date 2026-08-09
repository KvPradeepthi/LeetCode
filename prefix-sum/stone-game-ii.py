class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        dp = [[0] * (n + 1) for _ in range(n)]
        def solve(i, M):
            if 2 * M >= n - i:
                return suffix[i]
            if dp[i][M] != 0:
                return dp[i][M]
            best = float("-inf")
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                taken = suffix[i] - suffix[i + X]
                opponent = solve(i + X, max(M, X))
                current = taken - opponent
                best = max(best, current)
            dp[i][M] = best
            return best
        difference = solve(0, 1)
        total = suffix[0]
        return (total + difference) // 2