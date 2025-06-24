import heapq

def solution(scoville, K):
    answer = 0
    #섞은 음식 스코빌지수 = 제일 덜매운거 + (두번째로 덜매운거*2)
    #모든 음식 스코빌지수가 K 이상일때까지 반복
    #앞에꺼 두개 빼서 새 스코빌지수 heap 에 넣기 반복

    heapq.heapify(scoville)
    
    min_scoville = scoville[0]
    
    while min_scoville < K and len(scoville)>=2:
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)


        new_scoville = m1 + m2 * 2
        
        heapq.heappush(scoville, new_scoville)
        
        min_scoville = scoville[0]

        answer +=1
        # print(m1,m2, new_scoville, min_scoville, answer, scoville )
    
    return answer if min_scoville >=K else -1