class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        l = m + n
        merged_arr = []

        if m == 0 and n == 0:
            return 0
        elif m == 0:
            merged_arr = nums2
        elif n == 0:
            merged_arr = nums1
        else:   
            for num in nums1:
                merged_arr.append(num)

            for num in nums2:
                merged_arr.append(num)

            merged_arr.sort()

        if l % 2 != 0:
            mid_index = (l - 1) / 2
            median = merged_arr[int(mid_index)]
            return median
        else:
            mid_index1 = (l // 2) - 1
            mid_index2 = (l // 2)
            median = (merged_arr[int(mid_index1)] + merged_arr[int(mid_index2)]) / 2
            return median
