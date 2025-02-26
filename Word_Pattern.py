class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split()

        if len(split_s) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, split_s):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True
