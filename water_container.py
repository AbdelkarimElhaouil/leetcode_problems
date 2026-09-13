# 11. Container With Most Water

def maxArea(height: list[int]) -> int:
    start, end = 0, len(height) - 1
    max_area = 0
    current_area = 0
    while start < end:
        current_area = min(height[start], height[end]) * (end - start)
        if current_area >= max_area:
            max_area = current_area
        if height[start] <= height[end]:
            start += 1
        elif height[start] > height[end]:
            end -= 1
    return max_area