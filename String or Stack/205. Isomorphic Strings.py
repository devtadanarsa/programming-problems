def isomorphicString(s, t):
    if len(s) != len(t):
        return False
    
    mapOne = {}
    mapTwo = {}
    for i in range(len(s)):
        if s[i] in mapOne:
            if mapOne[s[i]] != t[i]:
                return False
        if t[i] in mapTwo:
            if mapTwo[t[i]] != s[i]:
                return False
        else:
            mapOne[s[i]] = t[i]
            mapTwo[t[i]] = s[i]
    
    return True
    
print(isomorphicString('paper', 'title'))