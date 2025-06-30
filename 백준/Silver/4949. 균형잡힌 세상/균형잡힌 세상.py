import sys
from collections import deque

while True:
    l = deque(sys.stdin.readline().rstrip())
    if l[0] == ".":
        break

    stack = []
    answer = 'yes'

    while l:
        char = l.popleft()
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break

    if stack: answer = 'no'
    print(answer)
