class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        f_str = s.split()
        last_word_index = len(f_str) - 1
        last_word_length = len(f_str[last_word_index])
        return last_word_length
