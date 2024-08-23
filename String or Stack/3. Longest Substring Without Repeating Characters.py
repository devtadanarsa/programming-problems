def lengthOfLongestSubstring(s):
    longestCount = 0
    
    for i in range(len(s)):
        count = 1
        tempMap = {}
        tempMap[s[i]] = True
        
        for j in range(i + 1, len(s)):
            if s[j] in tempMap:
                if longestCount < count:
                    longestCount = count
                
                break
            else:
                tempMap[s[j]] = True
                count += 1
                
        if longestCount < count:
            longestCount = count
    
    return longestCount
                
print(lengthOfLongestSubstring(' '))