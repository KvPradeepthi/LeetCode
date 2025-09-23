class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle negative and positive numbers
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits by converting to string and back to integer
        reversed_x = int(str(x)[::-1])
        
        # Apply the sign to the reversed number
        reversed_x *= sign
        
        # Check for overflow; return 0 if it exceeds 32-bit range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        return reversed_x
