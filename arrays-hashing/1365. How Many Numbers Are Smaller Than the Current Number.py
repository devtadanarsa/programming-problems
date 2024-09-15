def smallerNumbersThanCurrent(nums):
    sortedNums = list(nums)
    sortedNums.sort()

    result = []
    for num in nums:
        result.append(sortedNums.index(num))
    
    return result
    
print(smallerNumbersThanCurrent([7,7,7,8,8,8,8]))