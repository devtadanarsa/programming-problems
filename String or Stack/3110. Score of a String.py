def scoreOfString(s):
    result = 0
    for i in range(len(s) - 1):
        result += abs(ord(s[i]) - ord(s[i+1]))
    
    return result