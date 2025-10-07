from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        n = len(rains)
        ans = [-1] * n
        full_lakes = {}  # lake -> last day it rained
        dry_days = SortedList()  # indices of dry days (0s)
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.add(i)
                ans[i] = 1  # default value, may change later
            else:
                if lake in full_lakes:
                    # find a dry day after the last rain on this lake
                    idx = dry_days.bisect_right(full_lakes[lake])
                    if idx == len(dry_days):
                        return []  # flood occurs
                    dry_day_index = dry_days[idx]
                    ans[dry_day_index] = lake  # dry this lake on that day
                    dry_days.pop(idx)
                full_lakes[lake] = i
                ans[i] = -1
        return ans
