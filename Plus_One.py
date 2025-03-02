class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Traverse digits from right to left
        for i in range(n-1, -1, -1):
            # If digit is less than 9, add 1
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set current digit to 0 and continue
            digits[i] = 0

        # If all digits were 9s, then add a leading 1
        return [1] + digits
