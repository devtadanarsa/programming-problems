def findArray(pref):    
    result = [pref[0]]
    
    for i in range(1, len(pref)):
        result.append(pref[i] ^ pref[i - 1])
        
    return result

print(findArray([13]))