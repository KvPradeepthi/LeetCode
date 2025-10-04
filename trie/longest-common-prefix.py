class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as prefix
        prefix = strs[0]
        
        for s in strs[1:]:
            # Trim the prefix until it matches the start of string s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
