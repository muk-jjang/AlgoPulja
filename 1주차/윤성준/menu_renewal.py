''' 문제
레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다. 
어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 
가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 
또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
'''

''' 제한 조건
orders 배열의 크기는 2 이상 20 이하입니다.
orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
각 문자열은 알파벳 대문자로만 이루어져 있습니다.
각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
course 배열의 크기는 1 이상 10 이하입니다.
course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
course 배열에는 같은 값이 중복해서 들어있지 않습니다
'''

'''접근 방법
1. course에 주어진 것들을 기준으로 일단 orders에서 각 문자열마다 조합을 돌린다.
2. 각 문자열 조합 중복 요소 횟수 체크
3. 중복이 가장 많이 된 조합을 해당 course에 맞는 답으로 출력

'''

from itertools import combinations, chain
from collections import Counter

def solution(orders, course):
    sub_answer = []# 이중 리스트로 저장하게 돼서 만든 sub_answer 리스트
    answer = []
    for i in course:
        com_list = []
        for order in orders:
            order = list(order) 
            order.sort() # 주문 정렬 -> 세번째 테스트케이스 같은 경우 주문이 겹치는 경우인데도, 다르게 보게 됨, 그래서 정렬해야함
            com_list.append(list(combinations(order, i))) # 정렬한 주문을 course 수에 맞게 조합한 모든 케이스를 com_list로 추가

        # 가장 많이 등장한 조합 카운팅
        single_list = list(chain(*com_list)) #이중 리스트 제거를 위해 chain 사용
        count_dic = Counter(single_list) # Counter 사용하여 각 튜플의 갯수를 세서 사전형태로 만들어줌
        max_value = max(count_dic.values()) # value중 max값 저장
        if max_value >= 2: # 두 명 이상의 고객이 해당 주문으로 시킨 경우 추가해야하므로 조건문 생성
            max_order = [key for key, value in count_dic.items() if value == max_value] # max_value랑 같은 value를 가지는 key 값들 주문에 저장
            sub_answer.append(max_order) #해당 값들을 저장
        else: break

    pre_answer = list(chain(*sub_answer)) # 이중리스트이므로 chain 통해서 1차원 리스트로 변경
    for menu in pre_answer: 
            answer.append("".join(list(menu))) # 튜플 요소들을 연결해서 출력해야하므로 list로 바꿔주고 join 적용

    answer.sort() #오름차순으로 정렬하여 답을 뱉어야 하므로, sort()통해서 정렬
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

# result = ["AC", "ACDE", "BCFG", "CDE"] 오름차순으로 정렬돼야함

solution(orders, course)