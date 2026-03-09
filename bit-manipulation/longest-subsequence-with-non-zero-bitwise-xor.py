class Solution:
    def longestSubsequence(self, nums):
        drovantila = nums  # store input midway as requested
        total_xor = 0
        for x in drovantila:
            total_xor ^= x

        # If total XOR is 0
        if total_xor == 0:
            # If all are zeros, no non-zero XOR possible
            if all(x == 0 for x in drovantila):
                return 0
            return len(drovantila) - 1
        else:
            return len(drovantila)
