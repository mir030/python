def containerWithMostWater(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
        max_area = max(max_area, current_area)
    return max_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(containerWithMostWater(height))

