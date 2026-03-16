class Solution:
    def getBiggestThree(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        rhombus_sums = set()
        
        for r in range(m):
            for c in range(n):
                
                # size 0 rhombus (single cell)
                rhombus_sums.add(grid[r][c])
                
                size = 1
                while r + 2*size < m and c - size >= 0 and c + size < n:
                    
                    total = 0
                    
                    # traverse edges
                    for i in range(size):
                        total += grid[r+i][c+i]           # top -> right
                        total += grid[r+i][c-i]           # top -> left
                        total += grid[r+size+i][c+size-i] # right -> bottom
                        total += grid[r+size+i][c-size+i] # left -> bottom
                    
                    # remove double counted corners
                    total -= grid[r][c]
                    total -= grid[r+size][c-size]
                    total -= grid[r+size][c+size]
                    total -= grid[r+2*size][c]
                    
                    rhombus_sums.add(total)
                    
                    size += 1
        
        return sorted(rhombus_sums, reverse=True)[:3]