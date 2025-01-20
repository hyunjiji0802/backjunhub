def count_routers(houses, distance):
    count = 1
    last = houses[0]
    for house in houses[1:]:
        if house - last >= distance:
            count += 1
            last = house
    return count

def binary_search(houses, C, left, right):
    if left > right:
        return right
    
    mid = (left + right) // 2
    
    if count_routers(houses, mid) >= C:
        return binary_search(houses, C, mid + 1, right)
    else:
        return binary_search(houses, C, left, mid - 1)

def max_distance(houses, C):
    houses.sort()
    return binary_search(houses, C, 1, houses[-1] - houses[0])

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

print(max_distance(houses, C))
