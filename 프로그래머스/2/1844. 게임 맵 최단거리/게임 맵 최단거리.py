#  최솟값을 return  ->>> BFS
from collections import deque

def solution(maps):
    n = len(maps)        # 행
    m = len(maps[0])     # 열

    # 상하좌우 이동 좌표
    dx = [-1, 1, 0, 0]  # 상하
    dy = [0, 0, -1, 1]  # 좌우

    # 큐에 시작 위치 삽입 (x, y)
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 4방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위 밖은 제외
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이거나 방문한 곳은 제외
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:  # 방문하지 않은 길이라면
                maps[nx][ny] = maps[x][y] + 1  # 거리 갱신
                queue.append((nx, ny))

    # 도착점에 도달하지 못했다면 -1
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]

