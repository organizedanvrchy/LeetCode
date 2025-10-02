class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # Drink All Bottles
        empty_bottles = numBottles
        drink_sum = numBottles

        while empty_bottles >= numExchange:
            # Exchange Empty Bottles for 1 Full Bottle
            empty_bottles -= numExchange
            numExchange += 1

            # Drink Exchanged Full Bottle
            drink_sum += 1

            # Add Empty Bottle Back
            empty_bottles += 1

        return drink_sum
