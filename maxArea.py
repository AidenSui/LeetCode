def maxArea( height):
    if len(height) == 2:
        return min(height)
    area = []
    lastHeight = height[-1]
    for i in range(len(height)-1):
        h = min(height[i], lastHeight)
        l = len(height) - i - 1
        area.append(h * l)
    print("Area:", area)
    print()
    return max(maxArea(height[:-1]), max(area))

print(maxArea([4,3,2,1,4]))