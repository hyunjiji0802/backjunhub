from collections import deque
n = int(input())
map = []
apt = [] #아파트 수
for _ in range(n):
    tmp = [int(i) for i in input()]
    map.append(tmp)

#   상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(cur_x,cur_y):
    stack = deque([(cur_x, cur_y)])
    map[cur_y][cur_x]=0#현재 위치 0으로 초기화    
    apart_num = 1
    while stack:  # 전부 다 돌아서 스택이 빌 때 까지
        x,y =stack.pop() #최근 위치 하나 꺼내기
        for i in range(4):  #상하좌우 탐색
            if 0 <= y + dy[i] < n and 0 <= x + dx[i] < n and map[y + dy[i]][x + dx[i]] != 0:  # 범위 내에 있고 아파트이면
                map[y+dy[i]][x+dx[i]]=0 #왔던 장소이므로 다시 올 필요 없음. 따라서 0으로 변경
                stack.append([x + dx[i], y + dy[i]])
                apart_num+=1 #아파트 수 세기
    return apart_num

for y in range(n):
    for x in range(n):
        if map[y][x]==0: #아파트가 아니면 continue
            continue
        elif map[y][x]>0: #아파트 단지에 속하면 단지 탐색 -> dfs 결과로 아파트 수를 push
            apt.append(dfs(x,y))

apt.sort()
print(len(apt))
for i in apt:
    print(i)
