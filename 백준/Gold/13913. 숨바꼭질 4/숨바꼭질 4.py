import sys
from collections import deque
n,k = map(int,sys.stdin.readline().rstrip().split(' '))
l = [0 for i in range(100001)] #방문한 숫자 리스트

def bfs(n,k,l):
    t = 0
    r = []
    r.append(n)
    deq = deque([(r,t)]) #현재위치랑 현재시간 튜플 담기
    l[n] = 1
    if n>=k:
        print(n-k)
        print(*[n-i for i in range(n-k+1)])
        return  #걸어서 가야함

    while deq:
        root,cur_t = deq.popleft() #큐에서 하나 꺼냄
        cur = root[-1]
        if cur == k:  # 같으면 현재 시간 반환
            print(cur_t)
            print(*root)
            return
        # *2 이동
        if  0<= 2*cur <= 100000 and l[2*cur] ==0: #순간이동 위치에 방문하지 않았고 범위 내에 있다면
            l[2*cur] = 1
            deq.append((root+[cur*2],cur_t+1))
        # -1 이동
        if  0<= cur-1 <= 100000 and l[cur-1] ==0: #-1 이동 위치에 방문하지 않았고 범위 내에 있다면
            l[cur-1] = 1
            deq.append((root+[cur-1],cur_t+1))
        # +1 이동
        if  0<= cur+1 <= 100000 and l[cur+1] ==0: #+1 이동 위치에 방문하지 않았고 범위 내에 있다면
            l[cur+1] = 1
            deq.append((root+[cur+1],cur_t+1))

bfs(n,k,l)
