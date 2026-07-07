class Solution:
    def sumAndMultiply(self, n: int) -> int:
        lst=list(str(n))
        lst3=[]
        sm=''
        sum=0
        for i in lst:
            if i!='0':
                lst3.append(i)
                sm=sm+i
                sum=sum+int(i)
        if sm=='':
            return 0
        s=''.join(lst3)
        num=int(sm)
        return (num*sum)
        