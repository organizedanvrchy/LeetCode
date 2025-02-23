class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        mapped_chars = set()

        for char_s, char_t in zip(s, t):
            if char_s in map_s_t:
                if map_s_t[char_s] != char_t:
                    return False
            
            else:
                if char_t in mapped_chars:
                    return False
                map_s_t[char_s] = char_t
                mapped_chars.add(char_t)
            
        return True
