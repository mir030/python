def maxArea(height):
    max_area, current_area = 0, 0
    # for i in range(len(height)-1):
    #     for j in range(i, len(height)):
    #         current_area = min(height[i], height[j]) * (j-i)
    #         if current_area > max_area:
    #             max_area = current_area
    # return max_area

    # for i in range(len(height)):
    #     left = i + 1
    #     while left < len(height):
    #         current_area = min(height[i], height[left]) * (left - i)
    #         left += 1
    #         if current_area > max_area:
    #             max_area = current_area
    # return max_area

    left = 0
    right = len(height) - 1
    while left < right:
        current_area = min(height[left], height[right]) * (right-left)
        if current_area > max_area:
            max_area = current_area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
print(maxArea([1, 1]))