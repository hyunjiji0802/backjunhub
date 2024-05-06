from math import sqrt, ceil
from math import sqrt
def solution(r1,r2):
    x=0
    answer = 0
    while x<=r2:
        #식계산
        top_range = int(sqrt(r2**2-x**2))
        if x == 0:
            bottom_range = ceil(sqrt(r1**2-x**2))
            remove = top_range - bottom_range + 1
        elif x<=r1:
            bottom_range = ceil(sqrt(r1**2-x**2))
            y = top_range - bottom_range + 1
            answer+=y
        else:
            y = top_range + 1
            answer+=y
        x+=1
    answer-=remove
    # print(answer,remove)
    
    return answer*4 + remove*4