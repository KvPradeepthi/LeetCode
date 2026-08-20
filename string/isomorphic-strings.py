class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapst={}
        mapts={}
        for ch in range(len(s)):
            a=s[ch]
            b=t[ch]
            if a in mapst:
                if mapst[a]!=b:
                    return False
            if b in mapts:
                if mapts[b]!=a:
                    return False 
            mapst[a]=b
            mapts[b]=a
        return True
        