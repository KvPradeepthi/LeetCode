class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)

        answer = [-1] * n

        stack = []

        for i in range(2 * n):

            current = nums[i % n]

            while stack and nums[stack[-1]] < current:

                index = stack.pop()

                answer[index] = current

            if i < n:
                stack.append(i)

        return answer