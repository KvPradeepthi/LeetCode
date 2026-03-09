class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num=[]
        for i in nums:
            i=i*i
            num.append(i)
        num.sort()
        return num
