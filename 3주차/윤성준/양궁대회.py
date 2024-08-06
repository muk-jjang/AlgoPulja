from itertools import combinations_with_replacement as combs

def solution(n, info):
    answer = []


    for comb in combs(range(11), n): # 중복조합 lion이 쏠 수 있는 모든 조합 계산
        lion = [0]*10
        lion_sco, apeach_sco = 0, 0
        for i in comb:
            lion[10-i] += 1 # lion이 점수마다 몇 개를 쐈는지 구성
        
        
        for i in range(10):
            if lion[i] > info[i]:
                lion_sco += 10-i
            else: 
                apeach_sco += 10-i
        
        if lion_sco > apeach_sco:
            



    return answer