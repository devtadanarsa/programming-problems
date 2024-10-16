def differenceOfSum(nums):
    element_sum = sum(nums)
    digit_sum = sum([sum([int(i) for i in list(str(num))]) for num in nums])

    return abs(element_sum - digit_sum)

nums = [1,2,3,4]
print(differenceOfSum(nums))
