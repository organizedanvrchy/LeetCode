class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      # str.find(substring) returns the index of the first occurrence of substring in str, or -1 if not found.
        return haystack.find(needle)

# Alternative
# def strStr(self, haystack: str, needle: str) -> int:
#     # Special case: if needle is an empty string, return 0
#     if needle == "":
#         return 0

#     h_len = len(haystack)
#     n_len = len(needle)

#     # Loop through each possible starting index in haystack
#     for i in range(h_len - n_len + 1):
#         # Assume a match is found until proven otherwise
#         match = True
        
#         # Check if the substring starting at index i matches needle
#         for j in range(n_len):
#             if haystack[i + j] != needle[j]:
#                 match = False
#                 break  # Mismatch found; break out of the inner loop

#         # If a full match was found, return the starting index
#         if match:
#             return i

#     # If needle is not found, return -1
#     return -1
