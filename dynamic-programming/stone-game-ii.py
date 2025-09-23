class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        
        # To store the cumulative sum of stones starting from i to the end
        suffix_sum = [0] * (n + 1)
        
        # Build the suffix sum array
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        # Memoization table to store the best result for each (i, M)
        memo = [[0] * (n + 1) for _ in range(n)]
        
        # Helper function for the dynamic programming recursion
        def dp(i, M):
            # If we've reached the end, no stones can be taken
            if i == n:
                return 0
            
            # If we can take all remaining piles, return the sum
            if 2 * M >= n - i:
                return suffix_sum[i]
            
            # If we already computed this state, return the stored result
            if memo[i][M] > 0:
                return memo[i][M]
            
            # Try all possible choices of X and minimize Bob's gain
            best = 0
            for X in range(1, 2 * M + 1):
                best = max(best, suffix_sum[i] - dp(i + X, max(M, X)))
            
            memo[i][M] = best
            return best
        
        return dp(0, 1)

        