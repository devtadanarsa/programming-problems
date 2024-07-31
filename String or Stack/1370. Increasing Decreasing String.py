def sortString(s):
    hashMap = {}
    for char in s:
        if ord(char) not in hashMap:
            hashMap[ord(char)] = 1
        else:
            hashMap[ord(char)] += 1
    
    result = ""
    isAsc = True
    while len(hashMap) > 0:    
        if isAsc is True:
            for key in sorted(hashMap):
                result += chr(key)
                if hashMap[key] == 1:
                    hashMap.pop(key)
                else:
                    hashMap[key] -= 1
            isAsc = False
        else:
            for key in reversed(sorted(hashMap)):
                result += chr(key)
                if hashMap[key] == 1:
                    hashMap.pop(key)
                else:
                    hashMap[key] -= 1
            isAsc = True
    
    return result
            
print(sortString("cat"))