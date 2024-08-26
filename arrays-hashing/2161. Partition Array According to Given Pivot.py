def pivotArray(nums, pivot):
    smaller = []
    bigger = []
    same = []
    
    for num in nums:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            bigger.append(num)
        else:
            same.append(num)
            
    return smaller + same + bigger

print(pivotArray([9,12,5,10,14,3,10], 10))