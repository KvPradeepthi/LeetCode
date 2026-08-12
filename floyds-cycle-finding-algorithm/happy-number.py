class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        while n!=1 and n not in visited:
            visited.add(n)
            s=0
            while n>0:
                r=n%10
                s=s+(r*r)
                n=n//10
            n=s
        return n==1
        
            