from collections import deque
N, K = map(int, input().split())
A = deque(list(map(int,input().split()))) #내구도
belt = deque([False for _ in range(N)]) #벨트 위 로봇 T/F
step = 0 #단계 수
while True:
    #내구도 0인 칸 수가 K개 이상이면 과정 종료
    if A.count(0) >= K:
        print(step)
        break
    #1. 벨트 & 로봇 회전
    A.rotate(1)
    belt.rotate(1) #맨앞, 뒤는 False ->자동으로 내리기
    belt[0], belt[-1] = False, False
    # print(f"회전: {A} {belt}")
    #2. 로봇 있으면 한칸 더 직진, 내구도 감소
    if any(belt):
        #맨 뒤 로봇(=가장 먼저 올라간 로봇)부터 이동
        for i in range(N-1,0,-1):
            #이동하려는 칸에 로봇이 없고, 해당 칸 내구도가 1 이상이면 이동
            if belt[i-1] is True and belt[i] == False and A[i]>=1:
                belt[i-1], belt[i] = belt[i], belt[i-1]
                A[i]-=1
    #언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    if belt[-1] == True:
        belt[-1] = False

    # print(f"이동: {A} {belt}")
    #3. 올리는 위치 칸 내구도가 0이 아니면 로봇 올리기
    if A[0]>0:
        belt[0]=True
        A[0]-=1
    #단계 + 1
    # print(f"로봇: {A} {belt}")
    step+=1