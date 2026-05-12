class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)
        ans = 0
        current = 0
        for actual, minimum in tasks:
            ans = max(ans, current + minimum)
            current += actual
        return ans