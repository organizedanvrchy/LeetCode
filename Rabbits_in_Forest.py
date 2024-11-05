import math
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        rabbits = 0

        for k, freq in count.items():
            groupSize = k + 1
            groups = math.ceil(freq/groupSize)
            rabbits += groups * groupSize
        
        return rabbits
