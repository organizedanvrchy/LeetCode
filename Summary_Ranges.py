class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # If the input list is empty, return an empty list
        if not nums:
            return []

        res = []
        # Initialize start of current range
        start = nums[0]
      
        # Iterate through the list, starting from the second element
        for i in range(1, len(nums)):
            # End of current range
            end = nums[i - 1]

            # If the current number is not 
            # consecutive to the previous one, 
            # a gap is found
            if nums[i] != end + 1:
                # If the start of the range is 
                # the same as the previous number, 
                # it's a single number
                if start == end:
                    res.append(str(start))
                else:
                    # Otherwise, form a range "start->end"
                    res.append(f"{start}->{end}")
                # Start new range
                start = nums[i]

        # Handle last range
        if start == nums[-1]:
            # If it's a single number
            res.append(str(start))
        else:
            # If it's a range
            res.append(f"{start}->{nums[-1]}")

        return res
