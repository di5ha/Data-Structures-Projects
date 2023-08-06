def push(stack, element):
    stack.append(element)

def pop(stack):
    if not stack:
        return None
    return stack.pop()

def peek(stack):
    if not stack:
        return None
    return stack[-1]

# Initialize an empty list to use as a stack
stack = []

# Push elements onto the stack using the push() function
push(stack, 10)
push(stack, 20)
push(stack, 30)

# The stack now contains [10, 20, 30]

# Peek the topmost element without removing it
top_element = peek(stack)
print("Top element:", top_element)  # Output: Top element: 30

# The stack still contains [10, 20, 30]

# Pop the topmost element from the stack using the pop() function
popped_element = pop(stack)
print("Popped element:", popped_element)  # Output: Popped element: 30

# The stack now contains [10, 20]

# Peek again after popping
top_element = peek(stack)
print("Top element:", top_element)  # Output: Top element: 20

# The stack still contains [10, 20]
