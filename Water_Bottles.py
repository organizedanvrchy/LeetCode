class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink_sum = 0
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            exch_full_bottles = empty_bottles // numExchange
            empty_bottles = (empty_bottles % numExchange) + exch_full_bottles

            drink_sum += exch_full_bottles

        drink_sum += numBottles

        return drink_sum
