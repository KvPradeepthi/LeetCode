class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min=float('inf')
        max=0
        for i in range(0,n):
            if prices[i]<min:
                min=prices[i]
            prices[i]=prices[i]-min
            if prices[i]>max:
                max=prices[i]
        return max
            


        