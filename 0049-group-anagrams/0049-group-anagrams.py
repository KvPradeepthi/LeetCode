class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for ch in strs:
            key="".join(sorted(ch))
            if key in mp:
                mp[key].append(ch)
            else:
                mp[key]=[ch]
        return list(mp.values())

            
        