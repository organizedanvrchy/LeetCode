class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        numSet = set()

        # Iterate through nums array
        for n in nums:
            # Check for numbers forming valid arithmetic triplets
            if (n - diff) in numSet and (n - 2 * diff) in numSet:
                    count += 1
            # Add number to set for future checks
            numSet.add(n)
            
        return count
