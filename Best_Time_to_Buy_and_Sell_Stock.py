class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variable to store minimum price
        min_price = float('inf')
        # Initialize variable to store maximum profit
        max_profit = 0

        # Loop through prices in price list
        for p in prices:
            # Update minimum price if current price is lower
            if p < min_price:
                min_price = p
            else:
                # Calculate current profit if selling at current price
                profit = p - min_price
                
                # Update maximum profit if current profit if higher than previous maximum profit
                if profit > max_profit:
                    max_profit = profit
        
        # Return maximum profit (maximum profit will remain 0 if not profit is possible)
        return max_profit
