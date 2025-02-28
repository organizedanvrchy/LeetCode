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
