def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prefix = [nums[0]]
    suffix = [nums[len(nums) - 1]]
    
    for i in range(1, len(nums)):
        prefix.append(nums[i] * prefix[i - 1])
    
    idx = 0
    for i in range(len(nums) - 2, -1, -1):
        suffix.append(nums[i] * suffix[idx])
        idx += 1
    
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix[len(suffix) - 2])
        elif i == len(nums) - 1:
            result.append(prefix[len(suffix) - 2])
        else:
            temp = prefix[i - 1] * suffix[len(suffix) - 2 - i]
            result.append(temp)
    
    print(result)
    
productExceptSelf([-1,2])
