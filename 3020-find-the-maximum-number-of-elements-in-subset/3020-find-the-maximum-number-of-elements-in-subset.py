class Solution:
    def maximumLength(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = 1
        if 1 in freq:
            if freq[1] % 2 == 0:
                ans = freq[1] - 1
            else:
                ans = freq[1]
        for num in freq:
            if num == 1:
                continue
            current = num
            length = 0
            while current in freq:
                if freq[current] >= 2:
                    length += 2
                    current = current * current
                else:
                    length += 1
                    break
            if length % 2 == 0:
                length -= 1

            if length > ans:
                ans = length
        return ans