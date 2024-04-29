def solution(numbers):
    numbers = list(map(str,numbers)) #숫자를 문자열로 변환
    for _ in numbers:
        num = numbers.pop(0)
        numbers.append(num*4)

    bucket = [[] for _ in range(10)] #나머지 결과를 담을 버킷
    len_num = 4
    i = 0

    while i < len_num:
        for num in numbers:   #각 수의 자리수 비교, 나머지 r 를 버킷에 append
            #뒤에서 i 번째 수를 꺼냄,  append
            tmp_num = num[:len_num]
            r = int(tmp_num[-1+(-i)])
            bucket[r].append(num)

        numbers = []

        for nums in bucket: #버킷의 숫자를 앞에서부터 꺼내서 numbers에 append
            while nums :
                num = nums.pop(0)
                numbers.append(num)
        i +=1

    numbers.reverse()
    for _ in numbers:
        num = numbers.pop(0)

        numbers.append(num[:len(num)//4])

    answer = "".join(map(str,numbers))

    if answer == '0'*len(answer):
        return '0'
    else:
        return answer