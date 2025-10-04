from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            # If the combination is of length k, add it to result
            if len(path) == k:
                result.append(path[:])
                return
            # Explore further numbers to add
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)  # move to next number
                path.pop()  # backtrack

        backtrack(1, [])
        return result
