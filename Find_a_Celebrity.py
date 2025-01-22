# Provided Code from course. I was unable to complete this question on my own. 

def findCelebrity(n: int) -> int:
        # base case
	if n < 2:
		return -1
	stack = []
        # put all people to the stack
	for i in range(n):
		stack.append(i)
	left = stack.pop()
	right = stack.pop()
	potential_celebrity = left if not knows(left, right) else right
	while len(stack) > 0:
		if knows(left, right):
			potential_celebrity = right
			left = stack.pop()
		else:
			potential_celebrity = left
			right = stack.pop()
        # double check the potential celebrity
	for i in range(n):
		if i != potential_celebrity and (not knows(i, potential_celebrity) or knows(potential_celebrity, i)):
			return -1
	return potential_celebrity
