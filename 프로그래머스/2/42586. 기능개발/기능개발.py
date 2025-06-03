from math import ceil

def solution(progresses, speeds):
    answer = []
    
    days = []
    #남은 일수 계산 후 days에 저장
    for i in range(len(progresses)):
        days.append(ceil((100 - progresses[i]) / speeds[i]))
    
    days.reverse()

    cnt = 0
    maxnum = -1
    
    #뒤에서부터 pop하면서 max값과 비교
    while days:
        item = days.pop()        
        #비어있거나 max보다 작으면 append
        if cnt == 0 or maxnum >= item:
            cnt += 1
            maxnum = max(maxnum, item)
            # print(item, answer)
            
        #그렇지 않으면 다른날 기능개발 배포
        else:
            answer.append(cnt)
            cnt = 1
            maxnum = item  
            
    answer.append(cnt)
    
    return answer