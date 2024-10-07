def frequencySort(nums):
    num_dict = {}
    
    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1
    
    sorted_dict = dict(sorted(num_dict.items(), key=lambda x:x[1]))
    
    total_dict = {}
    for key in sorted_dict:
        if num_dict[key] in total_dict:
            total_dict[num_dict[key]].append(key)
        else:
            total_dict[num_dict[key]] = [key]

    for key, values in total_dict.items():
        if len(values) > 1:
            total_dict[key] = sorted(values, reverse=True)

    res = []
    for vals in total_dict.values():
        for val in vals:
            res.extend(num_dict[val] * [val])
        
    return res
                
            
print(frequencySort([-39,27,27,-11,-39,-11,-11,27,-11,-26,-33,-26,-11,0,-11,0,-26,27,-39,-26,0,27,-33,-33,27,0,27,27,-33,0,-11,-26,-11]))