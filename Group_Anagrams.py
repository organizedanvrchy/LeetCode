# LINK to Question: https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            # Sort string and find key
            key = ''.join(sorted(s))
            
            # Add original string to anagram list
            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(s)

        # Return grouped anagrams
        return list(anagrams.values())
