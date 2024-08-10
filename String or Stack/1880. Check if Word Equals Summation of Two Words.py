def isSumEqual(firstWord, secondWord, targetWord):
    strOne = strTwo = strThree = ""
    
    # turn first word into string
    for char in firstWord:
        charNum = (ord(char)) - 97
        
        if charNum == 0 and len(strOne) == 0:
            continue
        
        strOne = strOne + str(charNum)
        
    # turn second word into string
    for char in secondWord:
        charNum = (ord(char)) - 97
        
        if charNum == 0 and len(strTwo) == 0:
            continue
        
        strTwo = strTwo + str(charNum)
        
    # turn target word into string
    for char in targetWord:
        charNum = (ord(char)) - 97
        
        if charNum == 0 and len(strThree) == 0:
            continue
        
        strThree = strThree + str(charNum)
    
    return int(strOne or 0) + int(strTwo or 0) == int(strThree or 0)
    
print(isSumEqual('aaa', 'a', 'aaaa'))