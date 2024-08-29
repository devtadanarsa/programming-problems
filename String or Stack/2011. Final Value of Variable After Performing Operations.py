def finalValueAfterOperations(operations):
    res = 0
    
    for operation in operations:
        if operation == '--X' or operation == 'X--':
            res -= 1
        else:
            res += 1
    
    return res