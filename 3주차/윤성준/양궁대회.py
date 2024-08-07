from itertools import combinations_with_replacement as combs

'''
def solution(n, info):
    answer = []
    max_sco = -1

    for comb in combs(range(11), n): # 중복조합 lion이 쏠 수 있는 모든 조합 계산
        lion = [0]*11
        lion_sco, apeach_sco = 0, 0
        for i in comb:
            lion[10-i] += 1 # lion이 점수마다 몇 개를 쐈는지 구성
        
        for i in range(11):
            if lion[i] > info[i]:
                lion_sco += 10-i
            else: 
                apeach_sco += 10-i
        # print("lion", lion_sco)
        # print("apeach", apeach_sco)

        if lion_sco > apeach_sco and lion_sco >= max_sco:
            answer.append((lion_sco, lion[:]))
            max_sco = lion_sco
    
    if max_sco == -1:
        answer.append((0, -1))
    else:
        answer.sort(key = lambda x :(x[0], x[-1]), reverse=True)

    print(answer[0][1])
    return answer[0][1]
'''
def solution(n, info):
    answer = []
    max_sco = -1

    for comb in combs(range(11), n): # 중복조합 lion이 쏠 수 있는 모든 조합 계산
        lion = [0]*11
        lion_sco, apeach_sco = 0, 0
        for i in comb:
            lion[10-i] += 1 # lion이 점수마다 몇 개를 쐈는지 구성
        
        for i in range(11):
            if lion[i] == 0 and info[i] ==0:
                continue
            elif lion[i] > info[i]:
                lion_sco += 10-i
            else: 
                apeach_sco += 10-i
        # print("lion", lion_sco)
        # print("apeach", apeach_sco)

        if lion_sco > apeach_sco and lion_sco - apeach_sco >= max_sco:
            answer.append((lion_sco - apeach_sco, lion[:]))
            max_sco = lion_sco - apeach_sco
    
    if max_sco == -1:
        answer.append((0, -1))
    else:
        answer.sort(key = lambda x :(x[0], x[-1]), reverse=True)

    print(answer[0][1])
    return answer[0][1]


n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]


solution(n, info)