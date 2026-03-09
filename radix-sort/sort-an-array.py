class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
      n=len(nums)
      if n<=1:
        return nums
      m=n//2
      l=self.sortArray(nums[:m])
      r=self.sortArray(nums[m:])
      i=j=0
      res=[]
      while i<len(l) and j<len(r):
        if l[i]<r[j]:
            res.append(l[i])
            i=i+1
        else:
            res.append(r[j])
            j=j+1
      return res+l[i:]+r[j:]

