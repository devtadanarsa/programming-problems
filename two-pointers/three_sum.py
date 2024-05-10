def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    hashMap = {}
    
    for idx, num in enumerate(nums):
        hashMap[num] = idx
        
    result = set()
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            desired = (nums[i] + nums[j]) * -1
            if desired in hashMap:
                if hashMap[desired] != i and hashMap[desired] != j:
                    result.add(tuple(sorted([nums[i], nums[j], desired])))
    
    return result

print(threeSum([-1,0,1,2,-1,-4]))
            