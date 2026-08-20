class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        ans=-1
        for ch in s:
            freq[ch]=freq.get(ch,0)+1 
        for i,ch in enumerate(s):
            if freq[ch]==1:
                ans=i
                break
        return ans
                 