def findDuplicates(nums):
    hashMap = {}
    result = set()
    
    for num in nums:
        if num not in hashMap:
            hashMap[num] = 1
        else:
            result.add(num)
            
    return list(result)

print(findDuplicates([1,1,2,1,2]))