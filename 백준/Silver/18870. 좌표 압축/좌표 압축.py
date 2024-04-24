import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
sort_arr=sorted(list(set(arr)))

d = dict()

for i in range(len(sort_arr)):
    d[sort_arr[i]]=i

for id in arr:
    print(d[id],end=' ')