from collections import deque
t = int(input())
#   상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

#인접 노드 입력받기
for test_case in range(t):
    worm = 0
    m, n, k = map(int, input().split())
    farm = [[0 for i in range(m)]for j in range(n)]
    for _ in range(k):
        x,y = map(int,input().split()) #배추 위치 입력
        farm[y][x] = 1 #배추 심기
    for y in range(n):
        for x in range(m):
            if farm[y][x] == 1: #배추가 심어져 있으면
                farm[y][x] = 0 #0으로 초기화 (방문표시)
                worm += 1  # 지렁이 +1
                stack = deque([(x, y)]) #배추 심어진 범위 파악, dfs 수행
                while stack: #스택이 빌 때 까지
                    cur_x, cur_y = stack.pop()
                    for i in range(4):
                        if 0 <= cur_x + dx[i] < m and 0 <= cur_y + dy[i] < n and farm[cur_y+dy[i]][cur_x+dx[i]]==1: #범위 내에있고, 주변에 배추가 있으면
                            farm[cur_y+dy[i]][cur_x+dx[i]]=0 #0으로 초기화(방문표시)
                            stack.append([cur_x+dx[i],cur_y+dy[i]]) #해당 좌표 추가
    print(worm)
