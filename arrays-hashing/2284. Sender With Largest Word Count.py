def largestWordCount(messages, senders):
    dict = {}
    
    for i in range(len(senders)):
        words = len(messages[i].split(" "))
        
        if senders[i] in dict:
            dict[senders[i]] += words
        else:
            dict[senders[i]] = words

    max = 0
    for key in dict:
        if dict[key] > max:
            max = dict[key]
            sender = key
            
    return sender

messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders = ["Bob","Charlie"]

print(largestWordCount(messages, senders))