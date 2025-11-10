class Solution:
    def minOperations(self, nums: List[int]) -> int:
      # Greedy Monotonic Stack Approach
        stack = []
        ops = 0
        for num in nums:
            # If Stack is not Empty and Top of Stack is Greater than Current Number, Pop Top of Stack
            while stack and stack[-1] > num:
                stack.pop()
            # If Stack is Empty and Top of Stack is Lesser than Current Non-Zero Number, Push Element (Increment Operations Needed)
            if not stack or stack[-1] < num:
                if num > 0:
                    ops += 1
                    stack.append(num)
        
        return ops
      
