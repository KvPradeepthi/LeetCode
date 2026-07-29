from collections import defaultdict,deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        reverseGraph=defaultdict(list)
        indegree=[0]*n
        for node in range(n):
            for neighbor in graph[node]:
                reverseGraph[neighbor].append(node)
                indegree[node]+=1
        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        safe=[]
        while queue:
            node=queue.popleft()
            safe.append(node)
            for neighbor in reverseGraph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return sorted(safe)