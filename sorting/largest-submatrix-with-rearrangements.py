class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        
        # Step 1: Update heights in-place
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]
        
        # Step 2: For each row, sort heights to find the max area
        for r in range(m):
            # We sort the current row's heights in descending order
            current_row = sorted(matrix[r], reverse=True)
            
            for i in range(n):
                # The height is current_row[i], the width is (i + 1)
                ans = max(ans, current_row[i] * (i + 1))
                
        return ans