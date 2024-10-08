# LINK to Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringMaxLength = 0
        substringStart = 0
        charIndexMap = {}

        if len(s) <= 1:
            return len(s)
        
        for substringEnd in range(len(s)):
            if s[substringEnd] in charIndexMap and charIndexMap[s[substringEnd]] >= substringStart:
                substringStart = charIndexMap[s[substringEnd]] + 1
            else:
                substringMaxLength = max(substringMaxLength, substringEnd - substringStart + 1)

            charIndexMap[s[substringEnd]] = substringEnd

        return substringMaxLength
