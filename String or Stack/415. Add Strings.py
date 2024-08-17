import math

def addStrings(num1, num2):
    result = []
    
    ptrOne = len(num1) - 1
    ptrTwo = len(num2) - 1
    
    remainder = 0
    while ptrOne >= 0 or ptrTwo >= 0 :
        if ptrOne == -1:
            additionResult = int(num2[ptrTwo]) + remainder
            remainder = math.floor(additionResult/10)
            if additionResult >= 10:
                additionResult = additionResult % 10
                
            result.insert(0, str(additionResult))
            ptrTwo -= 1
            
        elif ptrTwo == -1:
            additionResult = int(num1[ptrOne]) + remainder
            remainder = math.floor(additionResult/10)
            if additionResult >= 10:
                additionResult = additionResult % 10
            
            result.insert(0, str(additionResult))
            ptrOne -= 1
            
        else:
            additionResult = int(num1[ptrOne]) + int(num2[ptrTwo]) + remainder
            if additionResult >= 10:
                remainder = math.floor(additionResult/10)
                additionResult = additionResult % 10
            
            result.insert(0, str(additionResult))
            ptrOne -= 1
            ptrTwo -= 1
    
    if remainder > 0:
        result.insert(0, str(remainder))
    
    return ''.join(result)

print(addStrings('456', '77'))
    