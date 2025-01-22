# Solution used from LeetCode as my solution was incorrect for some test cases. 

from collections import deque
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Step 1: Build the graph as an adjacency list
        g = [[] for _ in range(n + 1)]  # Graph representation: g[node] = list of neighbors
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Step 2: Initialize BFS queue and distance arrays
        # Queue holds tuples (current_node, visit_frequency)
        q = deque([(1, 1)])  # Start BFS from node 1 with visit frequency 1
        dist1 = [-1] * (n + 1)  # dist1[x]: Shortest time to reach node x
        dist2 = [-1] * (n + 1)  # dist2[x]: Second shortest time to reach node x
        dist1[1] = 0  # Time to reach node 1 is 0

        # Step 3: Perform BFS
        while q:
            x, freq = q.popleft()  # Dequeue current node and its visit frequency
            
            # Determine current time based on visit frequency
            t = dist1[x] if freq == 1 else dist2[x]

            # Adjust time if the traffic signal is red
            if (t // change) % 2:  # If current time is in the red phase
                t = change * (t // change + 1) + time  # Wait for green, then add travel time
            else:  # If current time is in the green phase
                t += time  # Add travel time immediately

            # Explore neighbors
            for y in g[x]:
                # Update shortest time for the neighbor if it hasn't been set
                if dist1[y] == -1:
                    dist1[y] = t
                    q.append((y, 1))  # Add neighbor with visit frequency 1
                # Update second shortest time for the neighbor if conditions are met
                elif dist2[y] == -1 and dist1[y] != t:
                    if y == n:  # If the neighbor is the destination, return second shortest time
                        return t
                    dist2[y] = t
                    q.append((y, 2))  # Add neighbor with visit frequency 2

        # Step 4: If no valid second shortest time is found, return 0
        return 0
