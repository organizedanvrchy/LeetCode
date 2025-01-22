from collections import deque

class RecentCounter:

    def __init__(self):
        # Create queue
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Add new ping to queue
        self.queue.append(t)

        # Remove request older than 3000 ms from queue
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.popleft()
        
        # Return length of queue with remaining requests
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
