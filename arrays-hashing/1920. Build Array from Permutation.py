def buildArray(nums):
    res = []
    
    for num in nums:
        res.append(nums[num])
    
    return res

print(buildArray([0,2,1,5,3,4]))