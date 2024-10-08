def maxWidthOfVerticalArea(points):
    xs = []
    xs = sorted([point[0] for point in points if point[0] not in xs])
    
    widest = 0
    for i in range(len(xs) - 1):
        area = xs[i + 1] - xs[i]
        if area > widest:
            widest = area
            
    return widest

print(maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))