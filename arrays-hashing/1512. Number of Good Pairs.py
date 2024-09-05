def numIdenticalPairs(nums):
    dict = {}
    
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = []
            
        dict[nums[i]].append(i)
    
    res = 0
    for key in dict:
        numAppeared = len(dict[key])
        
        if numAppeared > 1:
           res += numAppeared * (numAppeared - 1) / 2
    
    return res

print(numIdenticalPairs([1,2,3,1,1,3]))