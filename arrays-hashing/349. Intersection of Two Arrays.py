def intersection(nums1, nums2):
    hashMap = {}
    
    for num in nums1:
        if num not in hashMap:
            hashMap[num] = 1
        else:
            hashMap[num] += 1
    
    result = []
    for num in nums2:
        if num in hashMap and num not in result:
            result.append(num)
            
    return result

nums1 = [3]
nums2 = [3]

print(intersection(nums1, nums2))