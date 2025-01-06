def count_visible_buildings(N, heights):
    visible = [0] * N
    for i in range(N):
        max_slope = float('-inf')
        for j in range(i+1, N):
            slope = (heights[j] - heights[i]) / (j - i)
            if slope > max_slope:
                visible[i] += 1
                visible[j] += 1
                max_slope = slope
    return max(visible)

N = int(input())
heights = list(map(int, input().split()))
print(count_visible_buildings(N, heights))
