class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Using Built-In Python Functions
        # res = bin(int(a, 2) + int(b, 2))[2:]
        # return res

        # 2nd Solution
        
        # Initialize result as an empty list
        result = []
        # Initialize carry to 0
        carry = 0
        
        # Make both strings of equal length by padding the shorter one with leading zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        # Traverse both strings from the end (right to left)
        for i in range(max_len - 1, -1, -1):
            # Convert the characters to integers and add them along with the carry
            sum = int(a[i]) + int(b[i]) + carry
            
            # Compute the current bit (0 or 1) for the result
            result.append(str(sum % 2))
            
            # Compute the carry (either 0 or 1)
            carry = sum // 2
        
        # If there's a carry left after the final addition, add it to the result
        if carry:
            result.append('1')
        
        # The result list is in reverse order, so reverse it and join to form a string
        return ''.join(reversed(result))


        # 3rd solution        
#         result = []
#         carry = 0

#         # Start from last character in both string
#         i = len(a) - 1
#         j = len(b) - 1

#         while i >= 0 or j >= 0 or carry:
#             # Get bit from a or 0 if out of bounds
#             if i >= 0:
#                 bit_a = int(a[i])
#             else:
#                 bit_a = 0

#             # Get bit from b or 0 if out of bounds
#             if j >= 0:
#                 bit_b = int(b[j])
#             else:
#                 bit_b = 0

#             # Calculate the binary sum
#             binary_sum = bit_a + bit_b + carry
#             # Append last bit of the binary sum
#             result.append(str(binary_sum % 2))
#             # Update the carry
#             carry = binary_sum // 2

#             # Move to left bit in string (if any)
#             i -= 1
#             j -= 1

#         # Reverse and join list for resultant binary sum
#         output = ''.join(result[::-1])
#         return output
        
