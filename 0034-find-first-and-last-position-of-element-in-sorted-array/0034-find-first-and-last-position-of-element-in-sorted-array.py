class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def find_first():
            low,high=0,n-1
            first=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    first=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return first
        def find_last():
            low,high=0,n-1
            last=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    last=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return last
        return [find_first(),find_last()]
        

        