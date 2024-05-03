def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    ptrOne, ptrTwo = 0, len(s) - 1
    
    while ptrOne < ptrTwo:
        if not s[ptrOne].isalnum():
            ptrOne += 1
            continue
        elif not s[ptrTwo].isalnum():
            ptrTwo -= 1
            continue
        
        if s[ptrOne].lower() != s[ptrTwo].lower():
            return False
        
        ptrOne += 1
        ptrTwo -= 1
    
    return True

print(isPalindrome(" "))

# print(not "s".isalnum())