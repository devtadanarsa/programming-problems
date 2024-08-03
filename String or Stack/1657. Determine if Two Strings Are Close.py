def closeStrings(word1, word2):
    if len(word1) != len(word2):
        return False
    
    mapOne = {}
    mapTwo = {}
    
    for i in range(len(word1)):
        if word1[i] not in mapOne:
            mapOne[word1[i]] = 1
        else:
            mapOne[word1[i]] += 1
            
        if word2[i] not in mapTwo:
            mapTwo[word2[i]] = 1
        else:
            mapTwo[word2[i]] += 1
    
    for key in mapOne:
        if key not in mapTwo:
            return False
    
    arrOne = list(sorted(mapOne.values()))
    arrTwo = list(sorted(mapTwo.values()))

    return arrOne == arrTwo
    
closeStrings("cabbba", "aabbss")