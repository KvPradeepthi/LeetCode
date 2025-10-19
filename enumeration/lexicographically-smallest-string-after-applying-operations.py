from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        queue = deque([s])
        smallest = s

        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            smallest = min(smallest, curr)

            # Operation 1: Add 'a' to all odd indices
            arr = list(curr)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            added = ''.join(arr)

            # Operation 2: Rotate right by 'b' positions
            rotated = curr[-b:] + curr[:-b]

            # Add both new states to the queue
            if added not in visited:
                queue.append(added)
            if rotated not in visited:
                queue.append(rotated)

        return smallest
