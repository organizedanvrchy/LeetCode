stack = []
paren_map = {')': '(', '}': '{', ']': '['}

for p in s:
    # If current char is a closing bracket
    if p in paren_map:
        # Get last opened bracket
        top = stack.pop() if stack else '#'
        # Check if it matches the expected opening
        if paren_map[p] != top:
            print("False")
    # If current char is an opening bracket
    else:
        # Add char to stack
        stack.append(p)

# Stack should be empty if valid
if not stack:
    print('True')
