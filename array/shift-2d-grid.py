class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        while k>0:
            lastelement=grid[m-1][n-1]
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if j>0:
                        grid[i][j]=grid[i][j-1]
                    else:
                        grid[i][j]=grid[i-1][n-1]
            grid[0][0]=lastelement
            k=k-1
        return grid

        