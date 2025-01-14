from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
keyword = set()
for n in range(N):
    str = stdin.readline().rstrip()
    keyword.add(str)

for m in range(M):
    inputs = set(stdin.readline().rstrip().split(','))
    for input in inputs:
        if input in keyword:
            keyword.remove(input)
    # keyword = keyword.difference(inputs)
    print(len(keyword))
