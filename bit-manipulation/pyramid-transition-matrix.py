from typing import List
from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)

        for a, b, c in allowed:
            mp[(a, b)].append(c)

        def dfs(curr):
            if len(curr) == 1:
                return True

            def backtrack(i, path):
                if i == len(curr) - 1:
                    return dfs("".join(path))

                if (curr[i], curr[i+1]) not in mp:
                    return False

                for ch in mp[(curr[i], curr[i+1])]:
                    path.append(ch)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()

                return False

            return backtrack(0, [])

        return dfs(bottom)
