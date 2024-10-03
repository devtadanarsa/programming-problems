def findPermutationDifference(s, t):
    res = 0
    
    for i in range(len(s)):
        res += abs(i - t.index(s[i]))
    
    return res

print(findPermutationDifference("rwohu", "rwuoh"))