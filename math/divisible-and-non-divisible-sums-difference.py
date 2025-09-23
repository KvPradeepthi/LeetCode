class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # total sum of numbers from 1 to n
        total_sum = n * (n + 1) // 2
        
        # sum of multiples of m
        k = n // m
        multiples_sum = m * (k * (k + 1)) // 2
        
        # final answer
        return total_sum - 2 * multiples_sum

        