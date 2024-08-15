def judgeCircle(moves):
    horizontal = vertical = 0
    
    for move in moves:
        if move == 'L':
            horizontal -= 1
        elif move == 'R':
            horizontal += 1
        elif move == 'U':
            vertical += 1
        elif move == 'D':
            vertical -= 1
    
    return not (horizontal or vertical)

print(judgeCircle("UDULLRRD"))