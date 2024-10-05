import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        # Push 1st element in nums1 paired with all elements in nums2 onto heap
        # Consider upto k elements from nums1
        for u in range(min(k, len(nums1))):
            # (sum, index in nums1, index in nums2)                             
            heapq.heappush(minHeap, (nums1[u] + nums2[0], u, 0))        

        # Extract k smallest pairs
        while minHeap and len(res) < k:
            # Pop k smallest pairs from heap and add to "res" list
            sumPair, u, v = heapq.heappop(minHeap)
            res.append((nums1[u], nums2[v]))
            
            # If next element in nums2 exists, push next pair onto heap
            if v + 1 < len(nums2):
                nextSum = nums1[u] + nums2[v + 1]
                heapq.heappush(minHeap, (nextSum, u, v + 1))

        return res
