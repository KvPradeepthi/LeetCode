class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sums=0
        s=0
        for i in nums:
            if nums.count(i)>sums:
                sums=nums.count(i)
                s=i
        return s
            
        return sums
        