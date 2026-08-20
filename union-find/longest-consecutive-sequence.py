class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        longest=0
        for i in range(len(nums)):
            if nums[i]-1 not in nums:
                cur=nums[i]
                count=1
                while cur+1 in nums:
                    cur+=1
                    count+=1
                longest=max(count,longest)
        return longest



        