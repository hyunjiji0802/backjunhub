from sys import stdin
T = int(stdin.readline().rstrip())
N = 10001
dp = [0] * N
dp[0] = 1
# 순서 없이 1, 2, 3을 사용하는 조합을 구함
for num in [1, 2, 3]:  # 각 숫자를 순서대로 추가
    for i in range(num, N):
        dp[i] += dp[i - num]

for _ in range(T):
    n = int(stdin.readline().rstrip())
    print(dp[n])