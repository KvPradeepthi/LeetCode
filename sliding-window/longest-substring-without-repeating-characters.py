class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=res=0
        for right,ch in enumerate(s):
            if ch in seen and seen[ch]>=left:
                left=seen[ch]+1
            seen[ch]=right
            window=right-left+1
            if window>res:
                res=window
        return res