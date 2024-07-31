def numUniqueEmails(emails):
    unique = set()
    
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+', 1)[0]
        local = local.replace('.', '')
        
        newStr = local + domain
        unique.add(newStr)
    
    return len(unique)

arr = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(numUniqueEmails(arr))