class Solution:
    def calculate(self, s: str) -> int:
        stack= []
        curr = 0
        res = 0
        sign = 1

        for char in s:
            if char.isdigit():
                # Get number from string
                curr = curr * 10 + int(char)

            # Add number to res when a sign is met
            elif char in ['+', '-']:
                res += sign * curr
                curr = 0
                # Update sign for next number
                if char == '+':
                    # Positive
                    sign = 1
                else:
                    # Negative
                    sign = -1
            
            # When encountering open parentheses,
            # push current res and sign onto stack
            elif char == '(':
                stack.append(res)
                stack.append(sign)

                # Reset for next expression
                res = 0
                sign = 1

            # When encountering closed parentheses,
            # add current number to res then pop the
            # sign and previous res and combine them
            elif char == ')':
                res += sign * curr
                curr = 0

                res *= stack.pop()
                res += stack.pop()

            # Skip over spaces
            elif char == ' ':
                continue

        # Add last number to res
        res += sign * curr
        return res
