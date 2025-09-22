from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Get frequency of each element
        freq = Counter(nums)
        # Find max frequency
        max_freq = max(freq.values())
        total_freq = 0
        
        # Check for frequencies that match max frequency 
        # and get sum of max matching frequencies
        for f in freq.values():
            if f == max_freq:
                total_freq += f
            
        return total_freq
        
