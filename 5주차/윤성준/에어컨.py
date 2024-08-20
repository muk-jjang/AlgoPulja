'''접근방법
존나 어려움. 어떻게 풀어야할지 일단 생각이 안 남..  느낌상 DFS인디... 
승객 탑승시점 기준으로 실내온도 시작점을 쾌적온도 범위 사이로 지정하고 모두 탐색



'''

'''변수명
temperature: 실외온도
t1 ~ t2: 쾌적한 실내온도 범위
a(에어컨 상승 or 하락), b(에어컨 유지) : 에어컨 소비 전력 
onboard: 승객이 탑승중인 시간 
'''



def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    return answer