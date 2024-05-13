def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    brackets = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    
    for char in s:
        if char in brackets:
            if len(stack) == 0 or stack.pop() != brackets[char]:
                return False
        else:
            stack.append(char)
                     
    if len(stack) > 0:
        return False
    return True
            
print(isValid("()[]{}"))