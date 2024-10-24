# LINK to Questions: https://leetcode.com/problems/keys-and-rooms/description/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])  # Visit room 0 first
        queue = deque([0])  # Start queue from room 0

        # Using BFS to explore all neighboring rooms
        while queue:
            room = queue.popleft()

            # Collect keys in current room and check if they unlock another room
            for key in rooms[room]:
                if key not in visited:      # If room is unvisited
                    visited.add(key)        # Mark room as visited
                    queue.append(key)       # Add room to queue

        # If we visit all rooms, return True
        return len(visited) == len(rooms)
