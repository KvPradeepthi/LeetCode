class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange   # use empty bottles for exchange
            numExchange += 1       # exchange rate increases
            drunk += 1             # drink new full bottle
            empty += 1             # that bottle becomes empty

        return drunk
