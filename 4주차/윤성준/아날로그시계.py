'''접근방법
1. 초 단위로 움직이는 각도 계산 -> 주어진 시간 간격을 초단위로 바꿔서 while문을 돌린다
2. 각도가 같아지는 시점, 초침 각도가 시침이나 분침보다 커지는 시점에 알람 울림


'''

''' 
내가 푼거 아님. 초단위를 시침 분침 초침 기준으로 어떻게 바꿔야할 지 잘 감이 안 와서 블로그 찾아봄
'''

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    start_time = h1*60*60 + m1*60 + s1
    end_time  = h2*60*60 + m2*60 + s2

    #시작시간이 12를 가리키고 있는 경우
    if start_time == 0 or start_time == 60*60*12:
        ans += 1

    #시침, 분침, 초침 돌아가는 각도 계산
    # 시침 -> 1시간에 30도 1초에 30/60*60 -> 1/120도
    # 분침 -> 1초에 360/60*60도 -> 1/10도
    # 초침 -> 60초에 360도 -> 1초에 6도
    while start_time < end_time:
        rad_h = start_time / 120 % 360
        rad_m = start_time / 10 % 360
        rad_s = start_time * 6 % 360

        rad_h_next = (start_time+1) / 120 % 360
        rad_m_next = (start_time+1) / 10 % 360
        rad_s_next = (start_time+1) *6 % 360

        if rad_h_next == 0:
            rad_h_next =360
        if rad_m_next ==0:
            rad_m_next = 360
        if rad_s_next == 0:
            rad_s_next = 360

        if (rad_s < rad_h and rad_h_next <= rad_s_next):
            answer += 1
        
        if (rad_s < rad_m  and rad_m_next <= rad_s):
            answer += 1
        
        # if rad_h_next == rad_s_next and rad_m_next == rad_s_next:
        #     answer -= 1

       

        
        start_time += 1

    return answer

h1 , m1, s1, h2 ,m2, s2 = 0, 5, 30, 0, 7, 0

print(solution(h1, m1, s1, h2, m2, s2))