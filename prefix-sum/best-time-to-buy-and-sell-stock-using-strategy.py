class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        original = sum(strategy[i] * prices[i] for i in range(n))
        A = [strategy[i] * prices[i] for i in range(n)]
        B = prices[:]
        prefA = [0] * (n + 1)
        prefB = [0] * (n + 1)
        for i in range(n):
            prefA[i + 1] = prefA[i] + A[i]
            prefB[i + 1] = prefB[i] + B[i]

        half = k // 2
        best_delta = 0

        for l in range(n - k + 1):
            first = -(prefA[l + half] - prefA[l])
            second = (prefB[l + k] - prefB[l + half]) - (prefA[l + k] - prefA[l + half])
            delta = first + second
            best_delta = max(best_delta, delta)

        return original + best_delta

        
        