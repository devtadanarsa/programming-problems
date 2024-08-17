def canConstruct(ransomNote, magazine):
    magazineMap = {}
    
    # put magazine characters into the map
    for char in magazine:
        if char not in magazineMap:
            magazineMap[char] = 1
        else:
            magazineMap[char] += 1
            
    # put ransom note characters into the map
    for char in ransomNote:
        if char not in magazineMap:
            return False
        elif magazineMap[char] <= 0:
            return False
        
        magazineMap[char] -= 1
    
    return True

print(canConstruct('aa', 'aab'))
            
    