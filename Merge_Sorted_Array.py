class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1 = m - 1      # Pointer for last valid element in nums1
        point2 = n - 1      # Pointer for last valid element in nums2
        endpoint = m + n - 1     # Pointer for end of merged array

        # While elements exists and can be compared
        while point1 >= 0 and point2 >= 0:
            # Compare and place larger element at end
            if nums1[point1] > nums2[point2]:
                nums1[endpoint] = nums1[point1]
                point1 -= 1
            else:
                nums1[endpoint] = nums2[point2]
                point2 -= 1
            endpoint -= 1

        # If nums2 is not exhausted, place additional elements in nums1
        nums1[:point2 + 1] = nums2[:point2 + 1]


