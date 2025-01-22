class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for asteroid in asteroids:
            # If the current asteroid is moving to the right or the stack is empty, just add it
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # Handle collisions
                while stack and stack[-1] > 0:
                    # If the top of the stack is moving to the right, a collision occurs
                    if stack[-1] < abs(asteroid):
                        # The current asteroid destroys the top asteroid in the stack
                        stack.pop()
                        continue
                    elif stack[-1] == abs(asteroid):
                        # Both asteroids destroy each other
                        stack.pop()
                    break
                else:
                    # No collision, or asteroid is smaller than the ones moving to the left
                    stack.append(asteroid)
        
        return stack
