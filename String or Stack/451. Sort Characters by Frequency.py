def frequencySort(s):
    hashMap = {}
    
    for char in s:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
            
    arr = []
    for key in hashMap:
        inserted = False
        
        for i in range(len(arr)):
            if hashMap[key] >= hashMap[arr[i]]:
                inserted = True
                
                for j in range(hashMap[key]):
                    arr.insert(i, key)
                
                break
        
        if not inserted:
            for i in range(hashMap[key]):
                arr.append(key)
        
        inserted = False
    
    return ''.join(arr)
    
print(frequencySort("a"))
    