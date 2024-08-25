def findWords(words):
    firstRow = list("qwertyuiop")
    secondRow = list("asdfghjkl")
    thirdRow = list("zxcvbnm")
    
    result = []
    
    for word in words:        
        if word[0].lower() in firstRow:
            rowUsed = firstRow
        elif word[0].lower() in secondRow:
            rowUsed = secondRow
        else:
            rowUsed = thirdRow
        
        valid = True
        for char in word:
            if char.lower() not in rowUsed:
                valid = False
                break
        
        if valid:
            result.append(word)
    
    return result
                

print(findWords(["Hello","Alaska","Dad","Peace"]))