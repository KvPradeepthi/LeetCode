class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sums=0
        s=0
        for i in nums:
            if nums.count(i)>sums:
                s=count(i)
                sums=i
        return sums
            
        return sums
        