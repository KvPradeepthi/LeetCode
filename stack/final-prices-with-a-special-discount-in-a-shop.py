class Solution(object):
    def finalPrices(self, prices):
        # Create an array to store the final prices
        answer = prices[:]
        stack = []
        
        # Iterate from right to left
        for i in range(len(prices) - 1, -1, -1):
            # While the stack is not empty and the top of the stack is greater than the current price
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()  # Remove the top item from stack
            
            # If the stack is not empty, apply the discount from the element at the top of the stack
            if stack:
                answer[i] -= prices[stack[-1]]
            
            # Push the current index onto the stack
            stack.append(i)
        
        return answer

        
        