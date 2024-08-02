def minRemoveToMakeValid(s):
    openParentheses = 0
    result = ''
    
    for i in range(len(s)):
        if s[i] == ')':
            if openParentheses <= 0:
                continue
            else:
                openParentheses -= 1
            
        if s[i] == '(':
            openParentheses += 1
            
        result += s[i]
        
    if openParentheses > 0 :
        for i in range (len(result) - 1, -1, -1):
            if openParentheses == 0:
                break
            
            if result[i] == '(' :
                openParentheses -= 1
                result = result[:i] + result[i + 1:]

    return result

print(minRemoveToMakeValid('(())))((a'))