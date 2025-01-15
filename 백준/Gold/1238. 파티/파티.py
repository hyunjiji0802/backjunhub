import heapq
import sys

def dijkstra(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# 입력 처리
n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append((end, time))
    reverse_graph[end].append((start, time))

# X에서 각 마을로 가는 최단 시간 계산
from_x = dijkstra(graph, x)

# 각 마을에서 X로 가는 최단 시간 계산
to_x = dijkstra(reverse_graph, x)

# 왕복 시간 계산 및 최대값 찾기
max_time = 0
for i in range(1, n+1):
    round_trip = from_x[i] + to_x[i]
    max_time = max(max_time, round_trip)

# 결과 출력
print(max_time)
