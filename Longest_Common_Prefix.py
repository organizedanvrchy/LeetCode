class Solution:
    def charSame(self, i, strs):
        c = strs[0][i]
        for s in strs:
            if s[i] != c:
                return False
        return True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_len = float('inf')
        shortest = None

        for s in strs:
            l = len(s)
            if l < shortest_len:
                shortest_len = l
                shortest = s

        for i,l in enumerate(shortest):
            if not self.charSame(i, strs):
                return shortest[:i]
        
        return shortest
