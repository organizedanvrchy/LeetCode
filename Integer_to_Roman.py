# LINK to Question: https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        # Define list of Roman Numerals with corresponding integer values
        # in descending order 
        romanNumerals = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]

        # Create list to store results
        result = []

        # Iterate through each symbol-value pair in the Roman Numeral list then
        # append the Roman Numeral of the value that can still be subtracted
        # from that num to the result list.

        # eg. If num = 43, then the first val that num is greater than in the
        # romanNumerals list is 40 paired with symbol 'XL'. The symbol will be
        # appended to the result list and 40 will be subtracted from 43, leaving
        # 3. Then 3, which is only greater than 1, paired with symbol 'I', will
        # result in 'I' being appended to the result list and then leaving the
        # number 2 and so on. Until we eventually end up with the result list
        # being ['XL', 'I', 'I', 'I'] which will be joined into a single string.
  
        for roman, val in romanNumerals:
            while num >= val:
                result.append(roman)
                num -= val
        
        return ''.join(result)
