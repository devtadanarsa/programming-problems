def commonChars(words):
    str = ""
    
    for i, word in enumerate(words):
        if i == 0:
           str = word
           continue
       
        newStr = ""
        for char in str:
            if word.count(char) > 0:
                newStr += char
        
        str = newStr
    
    return list(str)
              
print(commonChars(["cool","lock","cook"]))  
    