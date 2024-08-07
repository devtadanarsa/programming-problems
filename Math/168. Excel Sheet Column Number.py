def titleToNumber(columnTitle):
    depth = result = 0
    for i in range(len(columnTitle) - 1, -1, -1):
        if i == len(columnTitle) - 1:
            result += ord(columnTitle[i]) - 64
        else:
            result += pow(26, depth) * (ord(columnTitle[i]) - 64)
            
        depth += 1
    
    return result

print(titleToNumber('BBA'))
        