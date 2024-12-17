from sys import stdin

# 입력 받기
N, K = map(int, stdin.readline().rstrip().split())
arr = [1 if s == 'H' else 0 for s in stdin.readline().rstrip()]

# 사람과 햄버거의 위치를 리스트로 저장
people = [i for i in range(N) if arr[i] == 0]  # 사람의 인덱스들
burgers = [i for i in range(N) if arr[i] == 1]  # 햄버거의 인덱스들

# 햄버거를 먹은 사람 수
answer = 0

# 햄버거를 먹을 수 있는지 확인
burger_idx = 0  # 햄버거 리스트를 순차적으로 살펴보기 위한 포인터

for person in people:
    # 현재 사람에게 먹을 수 있는 햄버거를 찾기 위해 인덱스 점프
    while burger_idx < len(burgers) and burgers[burger_idx] < person - K:
        burger_idx += 1
    
    if burger_idx < len(burgers) and abs(burgers[burger_idx] - person) <= K:
        # 만약 이 햄버거가 먹을 수 있다면
        answer += 1
        burger_idx += 1  # 이 햄버거는 더 이상 사용할 수 없으므로, 포인터 이동
    
# 결과 출력
print(answer)
