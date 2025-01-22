import collections
import heapq

def findCheapestPrice(n, flights, src, dst, k):
    # Step 1: Build the adjacency list
    f = collections.defaultdict(dict)
    for a, b, p in flights:
        f[a][b] = p  # Cost of flight from a to b

    # Step 2: Initialize the min-heap
    # (current_price, current_city, stops_remaining)
    heap = [(0, src, k + 1)]

    # Step 3: Process the heap
    while heap:
        # Pop the city with the lowest price
        p, i, k = heapq.heappop(heap)

        # If we reach the destination, return the price
        if i == dst:
            return p

        # If stops remain, explore the neighbors
        if k > 0:
            for j in f[i]:
                heapq.heappush(heap, (p + f[i][j], j, k - 1))

    # If no valid path is found, return -1
    return -1
