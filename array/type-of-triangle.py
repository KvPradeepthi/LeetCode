class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        
        # Check triangle inequality
        if not (a + b > c and a + c > b and b + c > a):
            return "none"
        
        # Classification
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"

        