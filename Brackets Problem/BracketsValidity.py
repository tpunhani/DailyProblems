# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

def isValid(self, s: str) -> bool:
    stack = []
    if len(s) == 1:
        return False
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
            print(stack[-1])
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and i=='}' and stack[-1]=='{':
            stack.pop()
        elif stack and i==']' and stack[-1]=='[':
            stack.pop()
        else:
            return False
        
    return stack==[]


