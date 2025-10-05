class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        total_drunk = 0
        
        while full > 0:
            # Drink all full bottles
            total_drunk += full
            empty += full
            full = 0
            
            # Exchange empty bottles for full ones
            full = empty // numExchange
            empty = empty % numExchange
            
        return total_drunk
