class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        maxArea = 0

        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = h * width

                maxArea = max(maxArea, area)

            stack.append(i)

        return maxArea