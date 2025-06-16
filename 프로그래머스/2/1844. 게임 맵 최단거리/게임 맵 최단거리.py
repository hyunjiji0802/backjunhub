from collections import deque

#  최솟값을 return  ->>> BFS
def solution(maps):
    n, m = len(maps), len(maps[0])  # 행, 열
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y, 1))  # 시작 좌표와 거리
        visited[x][y] = True

        while queue:
            x, y, dist = queue.popleft()

            if x == n - 1 and y == m - 1:
                return dist  # 도착하면 거리 리턴

            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))

        return -1  # 도달 실패

    return bfs(0, 0)
