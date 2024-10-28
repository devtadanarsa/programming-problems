def minimumOperations(nums):
    count = 0    
    nums = [num for num in nums if num > 0]
    
    while sum(nums) > 0:
        smallest = min(nums)
        nums = [num - smallest for num in nums if num - smallest > 0]
        count += 1
        
    return count

print(minimumOperations([0]))
        