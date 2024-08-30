def checkArithmeticSubarrays(nums, l, r):
    res = []
    
    for i in range(len(l)):
        arr = nums[l[i]:r[i] + 1]
        arr = sorted(arr)
        
        diff = arr[1] - arr[0]
        for j in range(len(arr) - 1):
            currDif =  arr[j + 1] - arr[j]
            
            if currDif != diff:
                res.append(False)
                break
        
        if len(res) == i:
            res.append(True)
    
    return res

nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]

print(checkArithmeticSubarrays(nums, l, r))