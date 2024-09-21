def buildArray(target, n):
    opr = []
    popDebt = 0
    
    stream = 1
    for targetNum in target:
        while stream < targetNum:
            popDebt += 1
            opr.append("Push")
            stream += 1
        
        for i in range(popDebt):
            opr.append("Pop")        
        
        stream += 1
        opr.append("Push")
        popDebt = 0
    
    return opr
            
print(buildArray([2,3,4], 4))