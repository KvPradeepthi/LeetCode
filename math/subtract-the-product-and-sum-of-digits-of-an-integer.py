class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        pro=1
        while n>0:
            r=n%10
            sum=sum+r
            pro=pro*r
            n=n//10
        return pro-sum
         
        