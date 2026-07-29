class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        while l<r:
            con=(r-l)*min(height[l],height[r])
            res=max(con,res)
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return res

            
        