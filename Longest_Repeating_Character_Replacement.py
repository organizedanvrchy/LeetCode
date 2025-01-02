class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Using sliding window technique

        left = 0 
        max_count = 0
        max_length = 0
        char_count = defaultdict(int)

        for right in range(len(s)):
            char_count[s[right]] += 1                        # Add current character to frequency map
            max_count = max(max_count, char_count[s[right]]) # Track char with highest frequency in window

            while(right - left + 1) - max_count > k:         # If number of changes required exceeds k, shrink window
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)   # Update the maximum length of a valid substring

        return max_length
