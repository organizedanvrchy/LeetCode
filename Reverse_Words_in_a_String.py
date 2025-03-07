class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_words = words[::-1]
        res = ' '.join(reverse_words)
        return res
