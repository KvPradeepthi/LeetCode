from bisect import bisect_left
from typing import List
class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:
        def solve(start1, dur1, start2, dur2):
            rides = sorted(zip(start2, dur2))
            starts = [s for s, d in rides]
            durs = [d for s, d in rides]
            n = len(rides)
            suf_min_dur = [0] * n
            suf_min_finish = [0] * n
            suf_min_dur[-1] = durs[-1]
            suf_min_finish[-1] = starts[-1] + durs[-1]
            for i in range(n - 2, -1, -1):
                suf_min_dur[i] = min(suf_min_dur[i + 1], durs[i])
                suf_min_finish[i] = min(
                    suf_min_finish[i + 1],
                    starts[i] + durs[i]
                )
            ans = float('inf')
            for s, d in zip(start1, dur1):
                finish = s + d
                idx = bisect_left(starts, finish)
                if idx < n:
                    ans = min(ans, suf_min_finish[idx])
                if idx > 0:
                    ans = min(ans, finish + min(durs[:idx]))
            return ans
        def preprocess(starts, durs):
            rides = sorted(zip(starts, durs))
            starts = [s for s, d in rides]
            durs = [d for s, d in rides]
            n = len(rides)
            pref = [0] * n
            pref[0] = durs[0]
            for i in range(1, n):
                pref[i] = min(pref[i - 1], durs[i])
            suf_finish = [0] * n
            suf_finish[-1] = starts[-1] + durs[-1]
            for i in range(n - 2, -1, -1):
                suf_finish[i] = min(
                    suf_finish[i + 1],
                    starts[i] + durs[i]
                )
            return starts, pref, suf_finish
        def calc(start1, dur1, start2, dur2):
            starts, pref, suf_finish = preprocess(start2, dur2)
            n = len(starts)
            ans = float('inf')
            for s, d in zip(start1, dur1):
                finish = s + d
                idx = bisect_left(starts, finish)
                if idx < n:
                    ans = min(ans, suf_finish[idx])
                if idx > 0:
                    ans = min(ans, finish + pref[idx - 1])
            return ans

        return min(
            calc(landStartTime, landDuration,
                 waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration,
                 landStartTime, landDuration)
        )