class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)
        # dp[i][j] will store the minimum score for polygon between i and j
        dp = [[0] * n for _ in range(n)]

        # gap = length of sub-polygon
        for gap in range(2, n):  # at least 3 vertices needed
            for i in range(n - gap):
                j = i + gap
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j]+values[i]*values[j] * values[k]
                    )
        return dp[0][n - 1]
