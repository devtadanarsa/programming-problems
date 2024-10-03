def canAliceWin(nums):
    two_digits = sum([num for num in nums if num >= 10])
    one_digits = sum(nums) - two_digits
    
    return one_digits != two_digits

print(canAliceWin([1,2,3,4,10]))