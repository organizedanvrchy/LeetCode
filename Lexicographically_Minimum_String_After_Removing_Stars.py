class Solution:
    def clearStars(self, s: str) -> str:
        from collections import defaultdict
        
        res = []
        # Track char positions in `res`
        positions = defaultdict(list)   
        
        for char in s:
            if char == "*":
                # Find smallest char in current stack
                min_char = min(positions)
                # Remove last position of smallest char
                last_pos = positions[min_char].pop()
                # Mark last occurrence of smallest char
                res[last_pos] = None
                # Clean up if no more of smallest char remains
                if not positions[min_char]:
                    del positions[min_char]
            else:
                res.append(char)
                positions[char].append(len(res) -1)

        # Remove `None` marked chars and return filtered string
        return ''.join([char for char in res if char is not None])
