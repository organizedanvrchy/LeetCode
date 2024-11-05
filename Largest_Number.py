class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings
        numToStr = list(map(str, nums))
        
        # Key used to "stretch" number to help with ordering
        def sortKey(x):
            return x * 10

        # Sort numbers using key helper above
        numToStr.sort(key = sortKey, reverse = True)

        largestNum = ''.join(numToStr)

        if largestNum[0] == '0':
            return '0'
        else:
            return largestNum
