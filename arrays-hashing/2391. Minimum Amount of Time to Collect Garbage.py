def garbageCollection(garbage, travel):
    dict = {}
    totalChars = len("".join(garbage))
    
    for i in range(len(garbage)):
        if 'G' in garbage[i]:
            dict['G'] = i
            
        if 'P' in garbage[i]:
            dict['P'] = i
            
        if 'M' in garbage[i]:
            dict['M'] = i
        
    travelTime = [0]
    for i in range(len(travel)):
        travelTime.append(travel[i] + travelTime[i])
    
    res = totalChars
    
    for key in dict:
        res += travelTime[dict[key]]
        
    return res
        
print(garbageCollection(["G","P","GP","GG"], [2,4,3]))
# garbageCollection(["G","P","GP","GG"], [2,4,3])