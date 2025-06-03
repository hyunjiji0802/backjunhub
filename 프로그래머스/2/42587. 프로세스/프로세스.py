def solution(priorities, location):
    answer = 0
    while priorities:
        #1. 프로세스 하나 꺼내기
        p = priorities.pop(0)
        print(p)
        #2. 우선순위 높은 프로세스 있으면 다시 큐에 넣기
        if len(priorities) > 0 and p < max(priorities):
            priorities.append(p)
            location = (location - 1) if (location - 1) >= 0 else (len(priorities) - 1)
        #3. 없으면 프로세스 실행하기
        else:
            answer+=1
            if location == 0:
                return answer            
            location -=1
        
    