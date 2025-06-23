def solution(clothes):
    answer = 1
    d = dict()
    for name,cloth in clothes:
        if d.get(cloth) is None:
            d[cloth] = set([name])
        else:
            d[cloth].add(name)
    

    for k, v in d.items():
        number = (len(v) + 1)
        answer *= number

    return answer - 1