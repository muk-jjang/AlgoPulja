# 회복한 시간 k초
# k*x만큼 회복됨
# t초만큼 회복하면? (k<=t) y만큼 추가 회복
def solution(bandage, health, attacks):
    answer = health
    # 연속성공횟수
    c = 0
    # 소요된 시간
    k = 0
    
    while answer > 0 and attacks:
        print(answer)
        k += 1
        if attacks[0][0] == k:
            c = 0
            answer -= attacks[0][1]
            attacks.pop(0)
            if answer <=0 :
                answer = -1
                break
            continue
        c += 1
        answer += bandage[1]
        if c == bandage[0]:
            answer += bandage[2]
            c = 0
        if answer >= health:
            answer = health
    return answer