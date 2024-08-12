'''접근방법
1. 공격 마지막 시간을 기준으로 for 문 -> 공격 시간의 최댓값이 1000이므로 시간복잡도 측면에서 어려움은 없어보임
2. attack의 시간이 아니라면 시간단위로 초당회복량을 더해줌 -> attack의 시간을 어떻게 매번 조건으로 확인해줄 것인가? attack 리스트를 dic으로 바꿈

이 문제의 핵심은 공격시간이 유니크 하다는 것, 즉 attack을 사전형으로 만들어서 풀어도 된다는 것


'''

def solution(bandage, health, attacks):
    attack_dic = dict(attacks)
    last_attack = attacks[-1][0]
    health_step = 1
    max_health = health

    for time_step in range(1, last_attack+1):
        # 해당 시간이 attack 시간 안에 존재하면 공격력만큼 체력 감소시키고 연속 성공 초기화
        if time_step in attack_dic: 
            health -= attack_dic[time_step]

            # 체력 0 이하되면 죽음
            if health <= 0 : 
                return -1
            
            health_step = 1
        # 체력이 최대 체력이랑 같으면 회복 없음
        elif health == max_health:
            continue
        #연속 성공하면 추가 회복 고려해주고 연속성공 초기화
        elif health_step == bandage[0]:
            health += (bandage[2] + bandage[1])
            health_step = 1
        # 초당회복량
        else:
            health += bandage[1]
            health_step += 1
    
    return health

bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5, 16], [8, 6]]	

print(solution(bandage, health, attacks))