def findMatrix(nums):
    dict = {}
    
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    
    keys = list(dict.keys())
    
    result = []
    while len(keys) > 0 :
        temp = []
        
        i = 0
        while i < len(keys):
            temp.append(keys[i])
            if dict[keys[i]] == 1:
                keys.pop(i)
            else:
                dict[keys[i]] -= 1
                i += 1
            
        result.append(temp)
    
    return result

print(findMatrix([1,2,3,4,4,4,5,3]))