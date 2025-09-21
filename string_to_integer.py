class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove whitespaces
        str_no_spaces = s.strip()
        # If string is empty, return 0
        if not str_no_spaces:
            return 0

        num = []
        sign = 1

        # Iterate through formatted string
        for idx, char in enumerate(str_no_spaces):
            # If first char is negative/positive sign
            if idx == 0:
                if char == "-":
                    sign *= -1
                    continue
                elif char == "+":
                    continue
            # If char is a number (0-9), add to array. If not, break.
            if char.isdigit():
                num.append(char)
            else:
                break

        # If array is empty, return 0
        if not num:
            return 0

        # Convert str to int
        res = int("".join(num)) * sign

        # Round to 32-bit integer range
        res = max(-2**31, min(2**31 - 1, res))

        return res
