def findTheWinner(n, k):
    circular = list(range(1, n + 1))
    
    i = 0
    count = 0
    while len(circular) > 1:
        count += 1
        if i >= len(circular):
            i = 0
            
        if count == k:
            circular.pop(i)
            count = 0
            
        else:
            i += 1
    
    return circular[0]

print(findTheWinner(5, 3))