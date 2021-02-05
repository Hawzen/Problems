def isValid(self, s: str) -> bool:
    duals = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = []
    for par in s:
        if len(stack) > 0 and duals.get(par, 0) == stack[-1]:
            stack.pop()
        else:
            stack.append(par)
    
    if stack:
        return False
    return True