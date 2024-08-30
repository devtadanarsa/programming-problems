def areAlmostEqual(s1, s2):
    strOneDiff = strTwoDiff = 0
    diffIdxOne = diffIdxTwo = []
    
    for i in range(len(s1)):
        if strOneDiff > 2:
            return False
        
        if s1[i] != s2[i]:
            strOneDiff += 1
            diffIdxOne.append(i)
            
    for i in range (len(s2)):
        if strTwoDiff > 2:
            return False
        
        if s2[i] != s1[i]:
            strTwoDiff += 1
            diffIdxTwo.append(i)
            
            
    if strOneDiff != strTwoDiff:
        return False
    
    if strOneDiff == len(s1) or strTwoDiff == len(s2):
        return False
    
    if diffIdxOne != diffIdxTwo:
        return False
    
    if strOneDiff == 1 or strTwoDiff == 1:
        return False
    
    if strOneDiff > 1 or strTwoDiff > 1:
        if s1[diffIdxOne[0]] != s2[diffIdxOne[1]]:
            return False
    
        if s2[diffIdxOne[0]] != s1[diffIdxOne[1]]:
            return False
    
    
    return True
        
            
print(areAlmostEqual("caa", "aaz"))