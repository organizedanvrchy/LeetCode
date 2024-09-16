class Solution:
    def decodeString(self, s: str) -> str:
        stack = []           # To store previous strings and numbers
        current_string = ""  # To store the current decoded string
        current_number = 0   # To store the current number for repetition

        for char in s:
            if char.isdigit():
                # Accumulate number (handles multi-digit numbers)
                current_number = current_number * 10 + int(char)
            elif char == '[':
                # Push the current string and number to stack, reset them
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0
            elif char == ']':
                # Pop from stack and repeat the current string accordingly
                previous_string, number = stack.pop()
                current_string = previous_string + current_string * number
            else:
                # Append characters to the current string
                current_string += char

        return current_string
