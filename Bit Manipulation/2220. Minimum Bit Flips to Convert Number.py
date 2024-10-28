def minBitFLips(start, goal):
    return format(start ^ goal, 'b').count('1')

print(minBitFLips(3,4))