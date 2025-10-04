class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                # Update the histogram heights
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            #
       