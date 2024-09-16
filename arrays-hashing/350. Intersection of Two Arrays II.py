def intersect(nums1, nums2):
    hashOne = {}
    hashTwo = {}
    
    for num in nums1:
        if num not in hashOne:
            hashOne[num] = 1
        else:
            hashOne[num] += 1
    
    for num in nums2:
        if num not in hashTwo:
            hashTwo[num] = 1
        else:
            hashTwo[num] += 1
    
    result = []    
    for key in hashOne:
        if key not in hashTwo:
            continue
        
        minCount = min(hashOne[key], hashTwo[key])
        
        for i in range(minCount):
            result.append(key)
    
    return result


nums1 = [0]
nums2= [0]
print(intersect(nums1, nums2))