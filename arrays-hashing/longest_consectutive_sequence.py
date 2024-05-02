def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hashMap = {}
    for num in nums:
        hashMap[num] = True
        
    longestCount = 0
    for i in range(len(nums)):
        if nums[i] - 1 not in hashMap:
            count = 1
            currentNum = nums[i]
            while currentNum + 1 in hashMap:
                count += 1
                currentNum += 1
            
            if count > longestCount:
                longestCount = count
            
            count = 0
            
        if longestCount > len(nums) / 2:
            break
        
    return longestCount

print(longestConsecutive([100,4,200,1,3,2]))
        