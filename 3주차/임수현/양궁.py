def solution(n, info):
    answer = []
    cost = [i+1 for i in info]
    
    # while문을 이용해 완전탐색 진행
    # 어케 조합하,,,,,
    # [0,0,,,0,0]에다가 하나씩 cost채워넣기
    rion=[0]*10
    for start_index in range(10):
        search_index = start_index
        while True:
            # 백지의 score판 shots의 변수로 복사, 화살개수도 coin으로 복사
            shots = rion
            coin = n
            for i in range(search_index,10):
                if coin>cost[i]:
                    shots[i]=cost[i]
            search_index+=1

    

            
    return answer