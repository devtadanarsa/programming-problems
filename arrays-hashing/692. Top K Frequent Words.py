def topKFrequent(words, k):
    hashMap = {}
    
    for word in words:
        if word not in hashMap:
            hashMap[word] = [word]
        else:
            hashMap[word].append(word)
            
    sortedList = sorted(list(hashMap.keys()))
    
    result = []
    for i in range(len(sortedList)):
        if len(result) < k:
            ptr = 0
            while ptr < len(result):
                if len(hashMap[result[ptr]]) < len(hashMap[sortedList[i]]):
                    break    
                ptr += 1
            
            result.insert(ptr, sortedList[i])
        else:
            for j in range(len(result)):
                if len(hashMap[sortedList[i]]) > len(hashMap[result[j]]):
                    result.insert(j, sortedList[i])
                    result.pop()
                    break   
                    
    return result

print(topKFrequent(["i","love"], 2))