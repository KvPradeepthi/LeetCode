from collections import defaultdict, deque
from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        if n == 1:
            return 0
        
        # Store indices for each value
        graph = defaultdict(list)
        
        for i, num in enumerate(arr):
            graph[num].append(i)
        
        # BFS
        q = deque([0])
        visited = {0}
        steps = 0
        
        while q:
            
            for _ in range(len(q)):
                i = q.popleft()
                
                # Reached last index
                if i == n - 1:
                    return steps
                
                # Possible next jumps
                neighbors = graph[arr[i]] + [i - 1, i + 1]
                
                for nei in neighbors:
                    
                    if 0 <= nei < n and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                
                # Clear to avoid repeated processing
                graph[arr[i]].clear()
            
            steps += 1
        
        return -1