class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # If empty list, immediately return 0
        if len(nums) == 0:
            return 0
        
        # Convert list to set
        num_set = set(nums)
        # Initialize variable to track 
        # length of longest sequence
        longest_seq = 0

        for num in num_set:
            # Start of a new sequence if `num - 1` is NOT in the set
            if num - 1 not in num_set:
                curr_num = num
                curr_seq = 1

                # Track length of current sequence
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_seq += 1

                # Update length of longest sequence
                longest_seq = max(longest_seq, curr_seq)

        return longest_seq
