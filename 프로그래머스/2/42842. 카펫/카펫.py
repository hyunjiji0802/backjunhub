def solution(brown, yellow):
    #brwon + yellow = 바깥 직사각형 넓이
    #yellow = 내부 직사각형 넓이
    #카펫 가로길이 >=세로길이
    #바깥 - 안쪽 직사각형의 가로, 세로 길이 차이는 2

    outer = brown + yellow #바깥 직사각형 넓이
    inner = yellow #내부 직사각형 넓이

    outer_set = set()
    for i in range(3,outer): #(가로,세로) 약수 셋 구하기. 노랑 격자에 둘러싸여있으니 최소 길이는 3부터 시작. 종료 조건 수정필요
        if outer%i==0 and i>=outer//i and outer//i>=3: #약수이고 가로>=세로이고 최소 세로길이가 3이상이면(내부 노랑격자 때문)
            outer_set.add((i,outer//i)) #바깥 직사각형 (가로,세로) 셋에 추가

    inner_set = set()
    for i in range(1,inner+1): #(가로,세로) 약수 셋 구하기.
        if inner%i==0 and i>=inner//i: #약수이고 가로>=세로라면
            inner_set.add((i,inner//i)) #내부 직사각형 (가로,세로) 셋에 추가

    #두 셋 돌면서 바깥 - 안쪽 직사각형의 가로, 세로 길이 차이는 2. 찾아보기
    for o in outer_set:
        for i in inner_set:
            # print('o:', o, 'i: ', i)
            if (o[0] - i[0] == 2) and (o[1] - i[1] == 2):
                return list(o)