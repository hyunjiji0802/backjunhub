from sys import stdin
N, K = map(int, stdin.readline().rstrip().split())

medal_dic = {}
for _ in range(N):
    nation, g, s, b = map(int, stdin.readline().rstrip().split())
    add_medals = tuple([g,s,b])
    medal_dic[nation] = add_medals

orders = list(set(medal_dic.values()))
orders.sort(key = lambda x: (-x[0],-x[1],-x[2]))

k_value = medal_dic[K]
print(orders.index(k_value)+1)
