# LINK to Question: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a map to store integer values of Roman numerals
        roman_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000  
        }

        total = 0
        n = len(s)

        # Iterate over the Roman Numeral string and check if current value is less than next value
        # (if that value exists) where, if it is less, subtract the value; otherwise, add the value. 
        # This handles the cases of IV, IX, CM, etc. 
        
        # eg. if we have "CMIX" this would give -100 since 'C' is less than 'M' and total = 0 
        # in the beginning. Then the loop moves to 'M' which is more than 'I' and would add 1000 
        # to total, resulting in total = 900 and so on.

        for i in range(n):
            if i < n - 1 and roman_int[s[i]] < roman_int[s[i + 1]]:
                total -= roman_int[s[i]]  
            else:
                total += roman_int[s[i]]
        return total
