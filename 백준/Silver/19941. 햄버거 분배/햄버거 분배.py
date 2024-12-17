from sys import stdin

# 입력 받기
N, K = map(int, stdin.readline().split())
arr = list(stdin.readline().strip())

# 최대 사람 수
max_people = 0

# 왼쪽부터 오른쪽으로 탐색
for i in range(N):
    if arr[i] == 'P':  # 사람이 나오면
        # 사람이 먹을 수 있는 햄버거 탐색 (왼쪽 -> 오른쪽 순서로)
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if arr[j] == 'H':  # 햄버거를 찾으면
                max_people += 1
                arr[j] = 'X'  # 해당 햄버거를 사용 처리
                break  # 한 사람은 한 개의 햄버거만 먹을 수 있으므로 탐색 종료

# 결과 출력
print(max_people)
