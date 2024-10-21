from itertools import permutations
#가능한 숫자 조합 생성 (앞에 0 고려)
#숫자 조합 리스트마다 소수 판독
def prime(n):
    i = 2 #나누는 수
    if n<=1: #1보다 작으면 소수X
        return False

    while n>i: #소수 판독
        if n%i == 0: #나누어떨어지면 소수X, false return
            return False
        i+=1

    return True

def solution(numbers):
    answer = 0

    for l in range(1,len(numbers)+1):
        p = set((permutations(numbers, l)))
        for i in p:
            if i[0]=='0': 
                continue
            else:
                num = int("".join(i))
                result = prime(num)
                if result:
                    answer+=1
    return answer