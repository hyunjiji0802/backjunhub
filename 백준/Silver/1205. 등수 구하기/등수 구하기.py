N, score, P = map(int, input().split())
if N == 0: #랭킹 리스트 아무도 없으면 1등
    print(1)
else: #랭킹 리스트 있으면
    rank = list(map(int,input().split()))
    answer = -1

    for i in range(N):
        if score > rank[i]:
            rank.insert(i, score)
            answer = rank.index(score) + 1
            break

    if len(rank) < P and answer == -1:
        rank.append(score)
        answer = rank.index(score) + 1

    print(answer)
