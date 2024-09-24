def reverseWords(s):
    words = s.split(' ')
    reversedWords = []
    
    for word in words:
        tmp = ''
        for i in range(len(word) - 1, -1, -1):
            tmp += word[i]
        reversedWords.append(tmp)
    
    result = ''
    for word in reversedWords:
        result += word + ' '
    
    result = result.strip()
    
    return result
        

print(reverseWords("Let's take LeetCode contest"))