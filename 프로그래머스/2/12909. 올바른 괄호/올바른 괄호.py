def solution(s):
    answer = True
    stack = []
    s = list(s)
    #닫는 괄호면 여는괄호 만날때 까지 stack 에 담기
    while s:
        item = s.pop()
        if item == ')':
            stack.append(item)
        elif item == '(' and len(stack)>0 and stack[-1] == ')':
            stack.pop()
        else:
            return False
        # print(s, stack, sep = "________")
    if stack: return False
    else: return True