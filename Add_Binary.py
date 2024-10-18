class Solution:
    def addBinary(self, a: str, b: str) -> str:
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
