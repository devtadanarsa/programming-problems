def leftRightDifference(nums):
    if len(nums) == 1:
        return [0]
    
    right = sum(nums) - nums[0]
    left = 0
    
    result = []
    for i in range(len(nums) - 1):
        result.append(abs(right - left))
        
        right -= nums[i + 1]
        left += nums[i]
    
    result.append(left)
    
    return result

print(leftRightDifference([1]))