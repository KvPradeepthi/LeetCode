class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        r=n-1
        while l<r:
            s=numbers[l]+numbers[r]
            if s==target:
                return l+1,r+1
            elif s<target:
                l=l+1
            else:
                r=r-1
            

            