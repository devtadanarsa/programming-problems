def removeOuterParentheses(s):
    depth = 0
    result = ""
    
    for char in s:
        if char == '(':
            if depth != 0:
                result = result + char
            depth += 1
        else:
            if depth > 1:
                result = result + char
            depth -= 1
    
    return result
        
print(removeOuterParentheses("(()())(())(()(()))"))
