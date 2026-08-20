class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1
        for ch in nums:
            if freq[ch]>(n//2):
                return ch 

        