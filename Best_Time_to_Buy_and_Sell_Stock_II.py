class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        # Iterate through array starting from 2nd element
        for i in range(1, n):
            # Check uf current price is higher than previous price
            if prices[i] > prices[i - 1]:
                curr_profit = prices[i] - prices[i - 1]
                # Add current profit to maximum profit
                max_profit += curr_profit

        return max_profit
