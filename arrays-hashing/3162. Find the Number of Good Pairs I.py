def numberOfPairs(nums1, nums2, k):
    count = 0
    
    for num1 in nums1:
        for num2 in nums2:
            if num1 < num2 * k:
                break
            
            if num1 % (num2 * k) == 0:
                count += 1
    
    return count
    
print(numberOfPairs([1,3,4], [1,3,4], 1))