from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)

        maxFreq = max(freq.values())

        countMax = 0

        for value in freq.values():

            if value == maxFreq:
                countMax += 1

        intervals = (maxFreq - 1) * (n + 1) + countMax

        return max(len(tasks), intervals)