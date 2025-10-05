class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1]  # start from the last row
        
        # iterate from second last row upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
        
        return dp[0]
