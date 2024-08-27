from collections import deque

# 자료형 설정에 따른 시간 초과... 라고 한다...
def solution(queue1, queue2):
    answer = 0
    limit = 3 * (len(queue1)) - 3
    q1 = deque(queue1); q2 = deque(queue2)
    sum1 = sum(queue1); sum2 = sum(queue2)
    # 불가능 조건 : 가장 큰 값이 총합/2보다 클 때, 총합이 홀수일 때
    while sum1!=sum2:
        if sum1 > sum2:
            cur = q1.popleft()
            sum2 += cur
            sum1 -= cur
            q2.append(cur)
        else:
            cur = q2.popleft()
            sum1 += cur
            sum2 -= cur
            q1.append(cur)
        answer += 1
        if answer > limit :
            answer = -1
            break
        
    return answer