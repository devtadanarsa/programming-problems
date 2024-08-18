def numJewelsInStones(jewels, stones):
    hashMap = {}
    
    for char in jewels:
        hashMap[char] =  True
    
    result = 0
    for char in stones:
        if char in hashMap:
            result += 1
            
    return result

print(numJewelsInStones('aA', 'aAA'))