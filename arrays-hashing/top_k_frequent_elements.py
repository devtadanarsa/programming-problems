def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hashTable = {}
    for num in nums:
        if num in hashTable:
            hashTable[num].append(num)
        else:
            hashTable[num] = [num]
            
    tempList = list(hashTable.values())
    tempList.sort(key=len, reverse=True)
    
    result = []
    for i in range(k):
        result.append(tempList[i][0])
    
    return result

