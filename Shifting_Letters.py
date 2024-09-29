class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # Convert string to list of characters
        s = list(s)

        # Accumulate shifts from end of list to beginning
        totalShift = 0
        for i in range(len(shifts) - 1, -1, -1):
            totalShift += shifts[i]
            # Handle wrap-around of 'z' to 'a'
            totalShift %= 26                      

            # Shift character at position i
            s[i] = chr((ord(s[i]) - ord('a') + totalShift) % 26 + ord('a'))

        return ''.join(s)


# Note: ord() returns the ASCII value of a character
# Note: chr() converts the ASCII value back to the corresponding character

# Note: LINE 14: I am effectively subtracting the ASCII value of 'a' from the
#                ASCII value of s[i] and converting the character to a zero-
#                indexed position in the alphabet. Then I add the accumulated
#                number of shifts to the character.

#                eg. if s[i] = a and totalShift = 2, then ord(s[i]) - ord('a') 
#                + totalShift = 97 - 97 + 2 = 2. 
#                Then 2 % 26 = 2 (no wrap-around)
#                Then 2 + ord('a') = 2 + 97 = 99
#                Then chr(99) = 'c'
