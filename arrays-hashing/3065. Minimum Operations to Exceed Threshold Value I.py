def minOperations(nums, k):
    smallerNums = 0
    
    for num in nums:
        if num < k:
            smallerNums += 1
    
    return smallerNums

print(minOperations([1,1,2,4,9], 9))