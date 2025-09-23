class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c=Counter(s)
        for i,ch in enumerate(s):
            if c[ch]==1:
                return i
        return -1