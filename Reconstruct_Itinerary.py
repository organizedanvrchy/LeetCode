from collections import deque, defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build the graph
        graph = defaultdict(list)
        for src, dest in sorted(tickets):
            graph[src].append(dest)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop(0)  # Get the lexicographically smallest
                dfs(next_airport)
            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]
