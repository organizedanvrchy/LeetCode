class Solution:
    def reverseBits(self, n: int) -> int:
        current_bits = str(bin(n))

        reversed = []
        for bit in current_bits[:1:-1]:
            reversed.append(bit)

        output_length = len(reversed)
        if output_length < 32:
            diff = 32 - output_length
            for n in range(diff):
                reversed.append('0')
            
        output = ''.join(reversed) 

        formatted_output = int(output, base=2)

        return formatted_output

# 2nd Solution
        # # Convert to binary string, remove '0b', and pad with leading zeros
        # current_bits = bin(n)[2:].zfill(32)

        # # Reverse the bits
        # reversed_bits = current_bits[::-1]

        # # Convert back to integer
        # formatted_output = int(reversed_bits, 2)

        # return formatted_output

# 3rd Solution
        # res = 0
        # for i in range(32):
        #     res = (res << 1) | (n & 1)
        #     n >>= 1
        # return res
