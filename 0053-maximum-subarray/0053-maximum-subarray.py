class Solution:
    def maxSubArray(self, lst: List[int]) -> int:
        maxsum=lst[0]
        csum=lst[0]
        for i in range(1,len(lst)):
            csum=max(lst[i],csum+lst[i])
            maxsum=max(csum,maxsum)
        return maxsum
