class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys={} 
        for ch in strs:
            key=''.join(sorted(ch))
            if key in keys:
                keys[key].append(ch)
            else:
                keys[key]=[ch]
        return list(keys.values())
            
        