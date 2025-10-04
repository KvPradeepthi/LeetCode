class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()  # splits by spaces and removes empty strings
        return len(words[-1])

        