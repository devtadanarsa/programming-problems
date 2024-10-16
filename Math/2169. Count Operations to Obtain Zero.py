def countOperations(num1, num2):
    count = 0
    while 1 not in [num1, num2] and 0 not in [num1, num2]:
        if max(num1, num2) == num1:
            num1 -= num2
        else:
            num2 -= num1
        
        count += 1
            
    if min(num1, num2) == 1:
        return count + max(num1, num2)
    
    return count

print(countOperations(10,10))