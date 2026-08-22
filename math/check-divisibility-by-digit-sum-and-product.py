class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        r=0
        t=n
        pro=1
        while n>0:
            r=n%10 
            s+=r 
            pro*=r
            n=n//10
        m=s+pro
        if t%m==0:
            return True
        else:
            return False