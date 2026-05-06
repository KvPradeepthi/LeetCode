class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=low+1
            elif nums[mid]>target:
                high=high-1
        return low
        
       