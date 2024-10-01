# LINK to Question: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert characters to lowercase and remove non-alphanumeric characters
        filteredString = ''.join(char.lower() for char in s if char.isalnum())

        # Check if string is equal to it's reversed version
        return filteredString == filteredString[::-1]


# class Solution:
#    def isPalindrome(self, s: str) -> bool:
#        filteredString = ''

#        for char in s:
#            if char.isalnum():
#                filteredString += char.lower()

#        return filteredString == filteredString[::-1]
