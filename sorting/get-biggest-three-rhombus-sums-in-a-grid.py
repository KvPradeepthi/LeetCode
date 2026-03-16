class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):
                
                # size 0 rhombus
                res.add(grid[r][c])

                size = 1
                while r - size >= 0 and r + size < m and c - size >= 0 and c + size < n:
                    s = 0

                    # top -> right
                    i, j = r - size, c
                    for k in range(size):
                        s += grid[i + k][j + k]

                    # right -> bottom
                    i, j = r, c + size
                    for k in range(size):
                        s += grid[i + k][j - k]

                    # bottom -> left
                    i, j = r + size, c
                    for k in range(size):
                        s += grid[i - k][j - k]

                    # left -> top
                    i, j = r, c - size
                    for k in range(size):
                        s += grid[i - k][j + k]

                    res.add(s)
                    size += 1

        return sorted(res, reverse=True)[:3]