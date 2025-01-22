class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weightedGraph = defaultdict(list)
        for u, v, w, in times:
            weightedGraph[u].append((v, w))

        # Dijkstra's Algorithm
        minHeap = [(0, k)]
        minTime = {}
        for i in range(1, n + 1):
            minTime[i] = float('inf')
        minTime[k] = 0

        while minHeap:
            currTime, u = heapq.heappop(minHeap)

            # If a better way to reach u exists, skip current
            if currTime > minTime[u]:
                continue
            
            # Check each neighbor of 'u'
            for v, w in weightedGraph[u]:
                time = currTime + w
                # Update minTime only if shorter path to 'v' is found
                if time < minTime[v]:
                    minTime[v] = time
                    heapq.heappush(minHeap, (time, v))

        # res is the max of the min times (time to reach furthest node)
        res = max(minTime.values())

        # Return -1 if node is unreachable, otherwise return res
        if res == float('inf'):
            return -1
        else:
            return res
