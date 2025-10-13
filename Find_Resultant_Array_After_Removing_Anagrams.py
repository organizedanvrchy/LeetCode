class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        idx = 1

        while idx < len(words):
            curr = sorted(words[idx])
            prev = sorted(words[idx - 1])
            # print(f"Curr: {curr}")
            # print(f"Prev: {prev}")
    
            if curr == prev:
                words.pop(idx)
            else:
                idx += 1
        return words
