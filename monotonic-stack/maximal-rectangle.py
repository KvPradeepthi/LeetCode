class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        def largestRectangleArea(heights: list[int]) -> int:
            stack = []
            heights.append(0)  # Sentinel
            area = 0
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    area = max(area, height * width)
                stack.append(i)
            heights.pop()
            return area
        
        for row in matrix:
            for i in range(n):
                # Update the heights histogram
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            # Calculate the largest rectangle for this histogram
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area
