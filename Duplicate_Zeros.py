class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        # Count zeros to be duplicated
        zeros = arr.count(0)

        # Working in reverse order, shift elements from end 
        # while avoiding removing necessary elements.
        for i in range(n - 1, -1, -1):
            # Shift element to right
            if i + zeros < n:
                arr[i + zeros] = arr[i]

            # If element equals 0, decrement zero count and 
            # make next element 0
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
