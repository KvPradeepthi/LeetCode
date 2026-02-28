class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lst=[]
        sets=set(nums)
        for i in range(1,n+1):
            if i not in sets:
                lst.append(i)
        return lst
        