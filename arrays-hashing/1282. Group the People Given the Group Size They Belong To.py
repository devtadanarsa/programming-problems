def groupThePeople(groupSizes):
    dict = {}
    
    for i in range(len(groupSizes)):
        if groupSizes[i] not in dict:
            dict[groupSizes[i]] = [i]
        else:
            dict[groupSizes[i]].append(i)
    
    result = []
    
    for key in dict:
        temp = []
        for i in range(len(dict[key])):
            temp.append(dict[key][i])
            
            if len(temp) == key:
                result.append(temp)
                temp = []

    return result
    
print(groupThePeople([500]))