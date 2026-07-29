class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        height = [[0] * n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if mat[i][j] == 1:
                    height[i][j] = 1 if i == 0 else height[i - 1][j] + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                min_height = float('inf')
                for k in range(j, -1, -1):
                    if height[i][k] == 0:
                        break
                    min_height = min(min_height, height[i][k])
                    ans += min_height
        return ans
        