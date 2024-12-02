from sys import stdin
import heapq
N, M = map(int,stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    #a ->b도 c만큼 비용, b->a도 c만큼 비용
    graph[a].append((b,c))
    graph[b].append((a,c))

max_position = 50000
# 각 위치까지의 최소 여물을 무한대로 초기화
meal = [float('inf')] * (max_position + 1)
# 우선순위 큐 초기화
queue = []
heapq.heappush(queue, (0, 1))  # (여물, 위치)
meal[1] = 0

while queue:
    current_meal, current_position = heapq.heappop(queue)
    # 찬홍이 위치에 도달했다면 최소 여물 반환
    if current_position == N:
        print(current_meal)
        break
    # 이미 기록된 최소 여물이 더 적으면 넘어감
    if current_meal > meal[current_position]:
        continue
    # 현재 노드에서 인접한 방문하지 않은 노드에 대해 다음 위치와 여물 계산
    for i in graph[current_position]:
        next_meal = current_meal + i[1]
        if next_meal < meal[i[0]]:
            meal[i[0]] = next_meal
            heapq.heappush(queue, (next_meal, i[0]))
