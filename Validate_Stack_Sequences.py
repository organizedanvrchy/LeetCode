class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p = 0

        for i in pushed:
            # Push element onto stack
            stack.append(i)

            # Check if top of stack matches current element in popped
            while stack and stack[-1] == popped[p]:
                # Pop from stack if there is a match
                stack.pop()
                # Move to next element in popped
                p += 1

        # If stack is empty, sequence matches
        return len(stack) == 0
