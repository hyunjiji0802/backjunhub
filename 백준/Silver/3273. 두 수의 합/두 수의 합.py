n = int(input())
l = list(map(int, input().split()))
x = int(input())


cnt=  0
l.sort()
# for i in range(n):
#     if i > x:
#         break
#     for j in range(i+1, n):
#         if l[i] + l[j] == x:
#             cnt += 1
# print(cnt)


p1 = 0
p2 = n - 1

while p1 < p2:
    total = l[p1] + l[p2]
    if total == x:
        cnt+=1
        p1+=1
    elif total > x:
        p2-=1
    elif total < x:
        p1+=1

print(cnt)
