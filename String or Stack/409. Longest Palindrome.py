def longestPalindrome(s):
    hashMap = {}
    for char in s:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
    
    oddArr = []
    
    result = 0
    for key in hashMap:
        if hashMap[key] % 2:
            if hashMap[key] < 3 and len(oddArr) != 0:
                continue
            oddArr.append(hashMap[key])
        else:
            result += hashMap[key]
    
    if len(oddArr) == 1:
        return result + oddArr[0]
    
    for i in range(len(oddArr)):
        if i == 0:
            result += oddArr[i]
        else:
            result += oddArr[i] - 1
            
    
    return result

print(longestPalindrome("abccccdd"))