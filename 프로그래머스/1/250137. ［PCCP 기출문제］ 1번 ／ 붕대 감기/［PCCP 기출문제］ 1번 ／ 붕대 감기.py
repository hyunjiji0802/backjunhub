def solution(bandage, health, attacks):
    trial_time, heal, extra_heal = bandage
    
    max_health = health #최대체력
    t = attacks[-1][0] #몬스터 마지막 공격 시간
    attacks = list(zip(*attacks))
    att_list = list(attacks)[0] #공격 시간 리스트
    damage_list = list(attacks)[1] #공격 데미지 리스트
    conti = 0 #연속 성공 시간
    
    i = 0
    while i<=t: #몬스터 마지막 공격 시간까지 반복
        if i in att_list:#공격 받았을경우
            id = att_list.index(i)
            conti = 0 #연속 성공시간 0
            health-=damage_list[id] #체력 감소
            
            if health<=0:#0 이하이면 사망
                return -1
        
        else:#공격하지 않는 경우
            health+=heal
            if i!=0:
                conti+=1
            if conti==trial_time: #trial_time동안 연속으로 붕대를 감는 데 성공하면
                conti = 0 #연속 성공 초기화
                health+=extra_heal #추가 체력 회복
            if health >= max_health: #최대 체력보다 많이 회복할 수 없음
                health = max_health 
                
        i+=1
        
    return health