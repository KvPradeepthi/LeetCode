class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(numbers):
            c=target-num
            if c in seen:
                return(seen[c]+1,i+1)
            seen[num]=i