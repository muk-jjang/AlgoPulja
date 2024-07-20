from itertools import combinations
from collections import Counter
def solution(orders, course):
    combs_result=[]
    # 조합을 활용하여 모든 course수의 음식 조합을 구한다. 이때 combinations을 이용하여 쉽게 모든 조합을 구함
    for order in orders:
        for i in course:
            if len(order)>=i:
                combs_tuple = combinations(order,i)
                # combinations을 이용해 나온 튜플 형식의 결과값을 우리가 최종적으로 구하려는 str값으로 변경하여 combs_result추가
                for comb_tuple in combs_tuple:
                    combs_result.append(''.join(sorted(comb_tuple)))
    # Counter을 이용하여 dic형태로 각 요소의 중복 개수를 구한다
    result = Counter(combs_result)

    # course수에 맞는 정답을 구하기 위해 'answer_dic[length]=[0,[]]'형태로 dictionary를 만든다. value에서 index 0 자리는 중복 개수, index 1은 정답 후보 단어 저장하는 리스트이다
    answer_dic={}
    for length in course:
        answer_dic[length]=[0,[]]
    for word in result.keys():
        # 기존보다 큰 종복 개수의 단어가 나오면 새롭게 갈아버린다
        if 1<result[word] and answer_dic[len(word)][0]<result[word]:
            answer_dic[len(word)][0]=result[word]
            answer_dic[len(word)][1]=[word]
        # 기존과 동일한 중복 개수이면 정답 후보 리스트에 추가한다
        elif 1<result[word] and answer_dic[len(word)][0]==result[word]:
            answer_dic[len(word)][1].append(word)
    # 정답 형식으로 맞춰준다
    answer = sorted([item for v in answer_dic.values() for item in v[1]])
    return answer
