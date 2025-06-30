import sys
K = int(input())

stack = []
sum_stack = []
for _ in range(K):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        sum_stack.append(stack.pop())
    else:
        stack.append(n)
print(sum(stack))