class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum=0
        lim=int(math.sqrt(num))
        for i in range(1,lim+1):
            if num%i==0:
                if i==num//i:
                    sum+=i
                else:
                    sum+=i
                    sum+=num//i
        if sum-num==num:
            return True
        else:
            return False