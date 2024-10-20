def maxDepth(s):
    currentDepth = 0
    maxDepth = 0
    
    for char in s:
        if char == '(':
            currentDepth += 1
        else:
            if currentDepth > maxDepth:
                maxDepth = currentDepth
            currentDepth -= 1
            
    return maxDepth