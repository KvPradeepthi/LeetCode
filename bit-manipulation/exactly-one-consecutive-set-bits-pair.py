class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        pairs=0
        while n>0:
            if (n&3)==3:
                pairs+=1
            n>>=1
        return pairs==1
        