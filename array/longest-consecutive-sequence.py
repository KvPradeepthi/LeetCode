class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        count=0
        longest=0
        for i in nums:
            if i-1 not in numset:
                cur=i
                count=1
                while cur+1 in numset:
                    cur+=1
                    count+=1
                longest=max(count,longest)
        return longest



        