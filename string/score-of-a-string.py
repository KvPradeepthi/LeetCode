class Solution:
    def scoreOfString(self, s: str) -> int:
        sumc=0
        for ch in range(len(s)-1):
            sumc+=abs(ord(s[ch])-ord(s[ch+1]))
        return sumc
            
        