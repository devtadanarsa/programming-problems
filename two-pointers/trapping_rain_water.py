def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    ptrOne = 0
    ptrTwo = len(height) - 1
    maxLeft = maxRight = 0
    trappedWater = 0
    
    while ptrOne < ptrTwo:
        if height[ptrOne] < height[ptrTwo]:
            if height[ptrOne] > maxLeft:
                maxLeft = height[ptrOne]
            else:
                trappedWater += maxLeft - height[ptrOne]
            ptrOne += 1
        else:
            if height[ptrTwo] > maxRight:
                maxRight = height[ptrTwo]
            else:
                trappedWater += maxRight - height[ptrTwo]
            ptrTwo -= 1
    
    return trappedWater

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
