'''접근방법
pop: 배열의 가장 앞의 요소 뽑기
insert: 배열의 가장 뒤로 넣기

1. 두 큐의 합을 구함, 합이 작은 큐를 기준으로 생각, 합이 큰 큐에서 하나씩 작은 큐로 옮김
2. 작은 큐의 합이 총합/2와 같아지면 횟수 반환, 커지면 작은큐의 합에서 요소 제외


작은 큐에서 먼저 요소를 뺏다고 해도 큰 큐의 가장 마지막으로 들어가기 때문에 큰 큐에서 작은 큐로 옮긴다는 기준을 잡아도 문제 없음

while 종료조건을 어떻게 줘야할까...?
작은 q에 있던 원소들이 큰 원소를 다 받고 본인의 원소가 다 큰 큐로 옮겨가면?

'''

# 테스트 100점 만점에 86.7
# def solution(queue1, queue2):
#     answer = 0
#     q1_sum = sum(queue1)
#     q2_sum = sum(queue2)
#     limit = len(queue1) * 2
    
#     while q1_sum != q2_sum:
#         if q1_sum > q2_sum:
#             item = queue1.pop(0)
#             queue2.append(item)
#             q1_sum -= item
#             q2_sum += item
#         elif q1_sum < q2_sum:
#             item = queue2.pop(0)
#             queue1.append(item)
#             q2_sum -= item
#             q1_sum += item
        
#         answer+=1

#         if answer > limit:
#             return -1
#     return answer

from collections import deque
# 100점 만점에 96.7
# 찾아보니까 위 방식은 성능적으로 불리한 연산이라고 함, 기존의 리스트에서 인덱스를 주고 pop하는 연산은 O(N)의 시간복잡도
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    limit = len(queue1) * 2 + 2
    
    while q1_sum != q2_sum:
        if q1_sum > q2_sum:
            item = queue1.popleft()
            queue2.append(item)
            q1_sum -= item
            q2_sum += item
        elif q1_sum < q2_sum:
            item = queue2.popleft()
            queue1.append(item)
            q2_sum -= item
            q1_sum += item
        
        answer+=1

        if answer > limit:
            return -1
    return answer

queue1 = [1,1]
queue2 = [1, 10, 1, 2]

print(solution(queue1, queue2))
