class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0  # track longest palindrome boundaries

        def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
            # expand while palindrome condition holds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return last valid palindrome boundaries
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindrome (center = i)
            l1, r1 = expandAroundCenter(i, i)
            # Even-length palindrome (center = i, i+1)
            l2, r2 = expandAroundCenter(i, i + 1)

            # check which is longer
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
