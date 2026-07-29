class Solution:
    def sortVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u'}
        vowel_list=[]
        for i,ch in enumerate(s):
            if ch in vowels:
                vowel_list.append(ch)
        from collections import Counter
        freq=Counter(vowel_list)
        first_index={}
        for i, ch in enumerate(s):
            if ch in vowels and ch not in first_index:
                first_index[ch]=i
        sorted_vowels=sorted(freq.keys(), key=lambda x:(-freq[x],first_index[x]))
        sorted_full=[]
        for ch in sorted_vowels:
            sorted_full.extend([ch]*freq[ch])
        result=list(s)
        idx=0
        for i in range(len(s)):
            if s[i] in vowels:
                result[i]=sorted_full[idx]
                idx+=1 
        return ''.join(result)