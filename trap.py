def trap(height) -> int:
    size = len(height)
    max_left = [0] * size
    max_right = [0] * size
    max_left[0] = height[0]
    max_right[-1] = height[-1]

    for i in range(1,size):
        max_left[i] = max(max_left[i-1], height[i])
        
    for i in range(size-2, -1, -1):
        max_right[i] = max(max_right[i+1], height[i])
        
    print(max_left)
    print(max_right)
    total = 0
    for i in range(size):
        total += min(max_left[i], max_right[i]) - height[i]
        
    return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))