def nextGreaterElement(nums1, nums2):
    stack = []
    oprResult = []
    
    for i in range(len(nums2) - 1, -1 , -1):
        while len(stack) > 0:
            if nums2[i] > stack[-1]:
                stack.pop()
            else:
                break
        
        if len(stack) == 0:
            oprResult.insert(0, -1)
        else:
            oprResult.insert(0, stack[-1])
        
        stack.append(nums2[i])
    
    result = []
    
    for num in nums1:
        idx = nums2.index(num)  
        result.append(oprResult[idx])
        
    return result
    
nums1 = [2,4,1,3]
nums2 = [2,1,4,3]

print(nextGreaterElement(nums1, nums2))
                