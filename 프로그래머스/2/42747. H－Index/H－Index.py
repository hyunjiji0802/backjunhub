def solution(citations):
    c_list = list(set((c, citations.count(c)) for c in citations)) #각 인용 회수 튜플을 담은 리스트
    c_list.sort(reverse = True) #인용 횟수 기준 내림차순 정렬
    #print(c_list)
    max_h = 0
    ref_papers = 0
    for c_tuple in c_list: #h번 이상 인용된 논문이 h편 이상인지 확인. 최댓값 비교
        ref_num=c_tuple[0] # = h
        ref_papers += c_tuple[1] #h번 이상 인용된 논문 수 (내림차순으로 계속 더하기)
        #print('h',ref_num, '인용된 논문 수',ref_papers, 'max',max_h)
        if ref_num >=ref_papers  and max_h<ref_papers: #h번 이상 인용된 논문 수가 h번 이상이고, 나머지 논문이 h번 이하 인용되고, max_h보다 크다면
            max_h = ref_papers #h값 업데이트

    return max_h