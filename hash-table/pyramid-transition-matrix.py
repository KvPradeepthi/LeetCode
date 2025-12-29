from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[(a, b)].append(c)

        memo = {}  # cache results for rows

        def dfs(curr):
            if curr in memo:
                return memo[curr]

            if len(curr) == 1:
                return True

            def backtrack(i, path):
                if i == len(curr) - 1:
                    return dfs("".join(path))

                key = (curr[i], curr[i + 1])
                if key not in mp:
                    return False

                for ch in mp[key]:
                    path.append(ch)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()

                return False

            memo[curr] = backtrack(0, [])
            return memo[curr]

        return dfs(bottom)
