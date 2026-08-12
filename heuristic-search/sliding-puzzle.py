from collections import deque
from typing import List
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(x) for row in board for x in row)
        target = '123450'

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        q = deque([(start, 0)])
        visited = {start}

        while q:
            state, steps = q.popleft()
            if state == target:
                return steps

            zero = state.index('0')
            for nxt in neighbors[zero]:
                lst = list(state)
                lst[zero], lst[nxt] = lst[nxt], lst[zero]
                new_state = ''.join(lst)
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, steps + 1))

        return -1
