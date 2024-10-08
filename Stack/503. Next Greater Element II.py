def nextGreaterElements(nums):
    stack = []
    result = []
    
    for i in range(len(nums) - 1, -1, -1):
        while len(stack) > 0:
            if nums[i] > stack[-1]:
                stack.pop()
            else:
                break
        
        if len(stack) == 0:
            result.insert(0, -1)
        else:
            result.insert(0, stack[-1])
        
        stack.append(nums[i])
    
    return result

print(nextGreaterElements([1,2,1]))