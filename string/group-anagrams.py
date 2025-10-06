from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))  # sort the string to get the key
            groups[key].append(s)
        
        return list(groups.values())
