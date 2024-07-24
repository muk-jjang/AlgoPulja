'''
문제 설명
카카오톡에서는 이모티콘을 무제한으로 사용할 수 있는 이모티콘 플러스 서비스 가입자 수를 늘리려고 합니다.
이를 위해 카카오톡에서는 이모티콘 할인 행사를 하는데, 목표는 다음과 같습니다.

이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
이모티콘 판매액을 최대한 늘리는 것.
1번 목표가 우선이며, 2번 목표가 그 다음입니다.

1번 목표 ->  최대한 많이 이모티콘 플러스 서비스 가입자를 만듦
2번 목표 -> 최대한 많이 이모티콘 플러스 서비스 가입자를 만들었으면 남은 사람들에게는 낮은 할인율을 적용해서 수익을 극대화

이모티콘 할인 행사는 다음과 같은 방식으로 진행됩니다.

n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매합니다.
이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
카카오톡 사용자들은 다음과 같은 기준을 따라 이모티콘을 사거나, 이모티콘 플러스 서비스에 가입합니다.

각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매합니다.
각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입합니다.
'''

# 일단은 이모티콘 최대 갯수가 7개이고 할인율이 4개이므로, 이모티콘을 기준으로 생각해보자!

# def solution(users, emoticons):
#     sale = [0.6, 0.7, 0.8, 0.9] # 40%, 30%. 20%, 10%
#     sale_price = [] # 각 이모티콘마다 할인 적용한 값을 저장할 리스트
#     sorted_users = sorted(users, key=lambda point: point[0])
#     for i in range(len(emoticons)): # 각 이모티콘 마다 할인 40, 30, 20, 10 적용한 것을 2차원 배열로 저장
#         sale_per = []
#         for j in range(len(sale)):
#             sale_per.append(emoticons[i] * sale[j])

#         sale_price.append(sale_per) 
    
#     print(sorted_users)
#     answer = []
#     return answer

''' 
1.이모티콘 할인 조합을 전부 계산 -> 일단 할인율이 4개, 이모티콘 갯수도 최대 7 4**7 총 2**14
2.각 조합을 유저를 돌며 계산 -> 1번 목표를 우선으로 조합 선택, 1번 목표가 같다면 매출액이 높은 조합으로 출력
'''
def solution(users, emoticons):
    discount = [10, 20, 30, 40] # 할인율 리스트
    dis_comb = [] #할인율 조합 넣어줄 리스트

    # DFS 통해서 모든 조합 계산, 재귀로 구현 -> 인턴 코테랑 완전 똑같은 유형
    def DFS(arr, index):
        if index == len(arr): # index가 emoticons 길이랑 같아지면 스톱하고, 모은 배열을 추가
            dis_comb.append(arr[:])
            return

        for i in discount: # discount list에서 discount들 하나씩 더해줌
            arr[index] += i
            DFS(arr, index+1) # 재귀 방식으로 모든 조합을 더해줌
            arr[index] = 0 # 해당 반복문이 1iter이 끝나고 나면 초기화 시켜줘야함 -> 새로운 조합 만들어야함

    DFS([0]*len(emoticons), 0)            

    sub = 0
    answer = [0, 0]

    for dis in dis_comb: # 각 조합마다 유저들이 구독을 할 것인지 아니면 그냥 조건에 맞는 것을 구매할 것인지
        result_sale = 0 # 구독 안 한 사람들한테 총 수익 -> 해당 조합에 대해 user 반복문이 다 돌면 초기화 해줘야함
        sub = 0 # 구독 수 -> 해당 조합에 대해 user 반복문이 다 돌면 초기화 해줘야함
        for user in users: 
            user_sale = 0
            for i in range(len(dis)):
                if user[0] <= dis[i]: # 유저의 discount 기준에 만족하면 해당 이모티콘 구매
                    user_sale += emoticons[i] * ((100-dis[i]) / 100) #해당 유저가 discount기준에 맞는 이모티콘을 총 구매한 금액

            if user_sale >= user[1]: # 총 구매한 금액에 본인만의 구독 기준보다 높으면, 그냥 구독을 한다
                sub += 1
            else: 
                result_sale += user_sale #  기준보다 낮으면 총 수익에 해당 수익을 더해줌 

        if sub > answer[0]: # 1번 조건  -> 구독자 수가 많으면 해당 조합 선택
            answer = [sub, int(result_sale)]
        elif sub == answer[0] and result_sale > answer[1]: # 2번 조건 -> 구독자 수가 같다면 -> 총 수익이 큰 조합을 선택
            answer = [sub, int(result_sale)]
            
    return answer

emoticons = [1300, 1500, 1600, 4900]
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]

emoticons1 = [7000, 9000]
users1 = [[40, 10000], [25, 10000]]

solution(users, emoticons)