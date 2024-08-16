def finalPrices(prices):
    stack = []
    result = []
    
    for i in range(len(prices) - 1, -1, -1):
        while len(stack) > 0:
            if prices[i] < stack[-1]:
                stack.pop()
            else:
                break
        
        if len(stack) == 0:
            result.insert(0, prices[i])
        else:
            result.insert(0, prices[i] - stack[-1])
        
        stack.append(prices[i])
    
    return result

print(finalPrices([1,2,3,4,5]))