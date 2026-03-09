class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        count = 1       
        length = 1       
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                length = 1
            count += length

        return count

        