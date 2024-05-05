def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ptrOne, ptrTwo = 0, len(height) - 1
    
    biggestArea = 0
    while ptrOne < ptrTwo:
        temp = 0
        if height[ptrOne] <= height[ptrTwo]:
            temp = height[ptrOne] * (ptrTwo - ptrOne)
            if height[ptrOne] == height[ptrTwo]:
                if height[ptrOne + 1] < height[ptrTwo - 1]:
                    ptrOne += 1
                else:
                    ptrTwo -= 1
            ptrOne += 1
        elif height[ptrOne] > height[ptrTwo]:
            temp = height[ptrTwo] * (ptrTwo - ptrOne)
            ptrTwo -= 1
            
        if temp > biggestArea:
            biggestArea = temp
    
    return biggestArea

print(maxArea([2,3,10,5,7,8,9]))