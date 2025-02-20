class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0                   # Keep track of count for current majority element candidate
        maj_num = None              # Initialize a variable to hold majority element candidate

        for num in nums:
            # Set current num as new candidate
            if count == 0:
                maj_num = num

            # Check is current num is same as candidate
            if num == maj_num:
                # Increase count if same
                count += 1
            else:
                # Decrease count if not same
                count -= 1
        
        # Verification step to count occurrences of candidate and check if count is greater than half the length of the list
        if nums.count(maj_num) > len(nums) // 2:
            # If true, return the candidate as the majority element
            return maj_num
        else:
            # Otherwise, print the message below. 
            print("No majority element found.")

      # Boyer–Moore Voting Algorithm for Majority Element

# Alternative Solution
  # n=len(nums)
  # nums.sort()
  # return nums[n//2]
