class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lst=[]
        lst=nums
        for i in range(n):
            lst.append(nums[i])
        return lst
            

        