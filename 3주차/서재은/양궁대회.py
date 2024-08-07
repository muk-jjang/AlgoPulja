import numpy as np
# 배열 두 개를 비교해 점수차를 return하는 함수 1
def compare_score(apeach, ryan):
    ap_score = 0; ryan_score = 0
    for i in range(10):
        if apeach[i]==ryan[i]==0:
            continue
        elif apeach[i] >= ryan[i] and apeach[i]>0:
            ap_score += (10-i)
        else:
            ryan_score += (10-i)
    return (ryan_score - ap_score)

# n을 10개로 분리해 가능한 경우들을 만드는 함수 -> DP 사용 ...
# 함수 1을 호출해 max 값 비교
def distribute_number(n, k, current=[]):
    if k == 1:
        yield current + [n]
    else:
        for i in range(n+1):
            yield from distribute_number(n - i, k - 1, current + [i])

def solution(n, info):
    answer = [-1]
    max_tmp = 0
    for l in list(distribute_number(n, 11)):
        tmp = compare_score(info, l)
        if tmp == max_tmp and tmp!=0:
            if np.where(np.array(l)>0)[0][-1] > np.where(np.array(answer)>0)[0][-1]:
                answer = l
        elif tmp > max_tmp:
            answer = l
            max_tmp = tmp
            
    return answer

if __name__=="__main__":
    print(solution(3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1]))