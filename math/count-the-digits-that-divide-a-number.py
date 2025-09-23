class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        t=num
        while num>0:
            r=num%10
            if r!=0 and t%r==0:
                count=count+1
            num=num//10
        return count      