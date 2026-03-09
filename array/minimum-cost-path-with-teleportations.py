from typing import List
import heapq
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**15
        
        
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0
        
    
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        
        
        activated = [0] * (k + 1)
        
        pq = [(0, 0, 0, 0)]  
        
        while pq:
            cost, i, j, t = heapq.heappop(pq)
            
            if cost > dist[i][j][t]:
                continue
            
            if i == m - 1 and j == n - 1:
                return cost
            
        
            if j + 1 < n:
                nc = cost + grid[i][j + 1]
                if nc < dist[i][j + 1][t]:
                    dist[i][j + 1][t] = nc
                    heapq.heappush(pq, (nc, i, j + 1, t))
            
            if i + 1 < m:
                nc = cost + grid[i + 1][j]
                if nc < dist[i + 1][j][t]:
                    dist[i + 1][j][t] = nc
                    heapq.heappush(pq, (nc, i + 1, j, t))
            
    
            if t < k:
                while activated[t] < len(cells) and cells[activated[t]][0] <= grid[i][j]:
                    _, x, y = cells[activated[t]]
                    activated[t] += 1
                    
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
        
        return -1
