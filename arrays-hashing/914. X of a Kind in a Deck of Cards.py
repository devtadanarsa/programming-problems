def gcd(num_one, num_two):
    if num_one == 0:
        return num_two

    return gcd(num_two % num_one, num_one)

def hasGroupsSizeX(deck):
    dict = {}
    
    for num in deck:
        if num not in dict:
            dict[num] = 0
        
        dict[num] += 1

    values = list(dict.values())
    
    for i in range(len(values) - 1):
        if i == 0:
            current = gcd(values[i], values[i + 1])
            if current == 1:
                return False
        else:
            if gcd(current, values[i + 1]) == 1 :
                return False
    
    return True

print(hasGroupsSizeX([1]))

# print(gcd(3,2))