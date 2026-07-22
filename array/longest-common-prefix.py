class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[len(strs)-1]
        a=""
        for i in range(len(strs)-1):
            if(first[i]==last[i]):
                a+=first[i]
            else:
                break
        return a
    

        
        