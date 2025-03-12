class Solution:
    def reverse(self, x: int) -> int:
        int_to_string = str(x)
        first_in = int_to_string[0]

        if first_in != "-":
            rev_int = int_to_string[::-1]
            rev_int = int(rev_int)
            if rev_int < -2**31 or rev_int > 2**31 - 1:
                return 0
            else:
                return int(rev_int)
                
        else:
            rev_int = int_to_string[:0:-1]
            rev_int = '-' + rev_int
            rev_int = int(rev_int)
            if rev_int < -2**31 or rev_int > 2**31 - 1:
                return 0
            else:
                return int(rev_int)

# Alternative Solution
# class Solution:
#     def reverse(self, x: int) -> int:
#         if x < 0:
#             sign = -1
#         else:
#             sign = 1

#         rev_int = int(str(abs(x))[::-1]) * sign

#         if rev_int < -2**31 or rev_int > 2**31 - 1:
#             return 0
#         else:
#             return rev_int
