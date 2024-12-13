from sys import stdin

# 입력 처리
N = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
total = int(stdin.readline().rstrip())

# 모든 요청이 배정될 수 있는 경우
if sum(arr) <= total:
    print(max(arr))
else:
    arr.sort()  # 요청 금액을 오름차순 정렬
    remaining_budget = total  # 남은 예산

    for i in range(N):
        # 현재 상한액 계산
        max_budget = remaining_budget // (N - i)
        if arr[i] <= max_budget:
            # 요청 금액이 상한액 이하인 경우 그대로 배정
            remaining_budget -= arr[i]
        else:
            # 요청 금액이 상한액 초과 -> 상한액 반환
            print(max_budget)
            break
