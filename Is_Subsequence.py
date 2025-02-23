class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subseq = []
        n = 0

        for m in t:
            if n < len(s) and s[n] == m:
                subseq.append(m)
                n += 1

        final_subseq = ''.join(subseq)   

        if final_subseq == s:
            return True
        else:
            return False
