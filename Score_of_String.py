class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_arr = []
        score = 0
        for char in s:
            ascii_val = ord(char)
            ascii_arr.append(ascii_val)

        for i in range(len(ascii_arr) - 1):
            score += abs(ascii_arr[i] - ascii_arr[i + 1])

        return score

# Alternative
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(0, len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        return score

        
