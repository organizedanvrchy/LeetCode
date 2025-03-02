class Solution:
    def hammingWeight(self, n: int) -> int:
      # convert decimal number into binary  
      n_binary = bin(n)

      # Initialize count
      count = 0

      # Go through string of binary digits and count the 1s
      for b in n_binary:
          if b == '1':
              count += 1
            
      # Return the total number of 1s
      return count    
