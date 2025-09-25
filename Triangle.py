class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Dynamic Programming Approach
        if not triangle:
            return 0

        # Create a dp array to hold minimum path sums, starting from current bottom layer (or row)
        dp = triangle[-1].copy() # Copy avoids mutating original list

        # Iterate from second to last layer and upwards to top layer
        for layer in range(len(triangle) -2, -1, -1):
            for idx in range(len(triangle[layer])):
                # Find minimum path sum for position (layer, idx),
                # this is its value plus the min of the two adjacent
                # items in the dp layer below. 
                dp[idx] = triangle[layer][idx] + min(dp[idx], dp[idx + 1])

        return dp[0]

        # min_sum = 0

        # for layer, num in enumerate(triangle):
        #     # Initialize a minimum number
        #     min_num = (float('inf'))
        #     # Sort list in ascending order
        #     triangle[layer].sort()
        #     # Iterate through sorted list and add minimum number to sum *** Destroys ordering -- Doesn't work for this ***
        #     for num in triangle[layer]:
        #         if num < min_num:
        #             # Store minimum number for layer
        #             min_num = num
        #             # Add minimum number to sum
        #             min_sum += min_num

        # return min_sum
