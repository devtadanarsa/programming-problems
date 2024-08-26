import math
import sys

def shortestToChar(s, c):
    targetIdx = []
    
    for index, char in enumerate(s):
        if char == c:
            targetIdx.append(index)
            
    result = []
    for index, char in enumerate(s):
        if char == c:
            result.append(0)
        else:
            smallestIdx = -1
            for num in targetIdx:                
                if abs(index - num) < smallestIdx or smallestIdx == -1:
                    smallestIdx = abs(index - num)
            
            result.append(smallestIdx)
                    
    return result

print(shortestToChar("aaabaaac", 'c'))
            