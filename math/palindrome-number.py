class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Create a reversed version of the number
        original = x
        reversed_num = 0

        while x != 0:
            # Extract the last digit of x
            digit = x % 10
            # Append digit to reversed_num
            reversed_num = reversed_num * 10 + digit
            # Remove the last digit from x
            x = x // 10

        # Compare the reversed number with the original number
        return original == reversed_num

        """
        :type x: int
        :rtype: bool
        """
        