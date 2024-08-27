def minOperations(boxes):
    ballPositions = []
    
    for i in range(len(boxes)):
        if boxes[i] == '1':
            ballPositions.append(i)
    
    result = []
    
    for i in range(len(boxes)):
        temp = 0
        for position in ballPositions:
            temp += abs(position - i)
        
        result.append(temp)
    
    return result
    
print(minOperations('011110'))
            