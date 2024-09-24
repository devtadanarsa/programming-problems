def getSneakyNumbers(nums):
    res = []
    nums_len = len(nums)
    
    for i in range(nums_len - 1):
        num = nums[i]
        if num in nums[i + 1: nums_len]:
            if not num in res:
                res.append(num)
    
    return res

print(getSneakyNumbers([2,2,5,4,4,]))
        