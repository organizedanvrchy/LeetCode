# LINK to Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substringMaxLength = 0
        substringStart = 0
        charIndexMap = {}

        if len(s) <= 1:
            return len(s)
        
        for charIndex in range(len(s)):
            if s[charIndex] in charIndexMap and charIndexMap[s[charIndex]] >= substringStart:
                substringStart = charIndexMap[s[charIndex]] + 1
            else:
                substringMaxLength = max(substringMaxLength, charIndex - substringStart + 1)

            charIndexMap[s[charIndex]] = charIndex

        return substringMaxLength
