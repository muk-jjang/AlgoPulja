# temp < t1 : [0,b,a] or temp > t2 : [a,b,0]
# 아이디어는 있는데 구현을 못한다 ... 자료구조 공부가 부족한듯

def solution(temp, t1, t2, a, b, onboard):
    dc = [0,b,a]
    graph = [[(0,temp)]]
    if temp < t1:
        dt = [-1,0,1]
    elif temp > t2:
        dt = [1,0,-1]

    # 그래프를 생성한다.
    for cur in onboard[1:]:
        tmp_list = []
        for node in graph[-1]:
            cost, tmp = node
            for i in range(3):
                new_tmp = tmp + dt[i]
                if i == 0 and temp == tmp:
                    new_tmp = tmp
                if cur == 0:
                    tmp_list.append((cost+dc[i], new_tmp))
                else:
                    if not (t1<=new_tmp<=t2):
                        continue
                    tmp_list.append((cost+dc[i], new_tmp))
        graph.append(tmp_list)
        #print(graph)
    return min(graph[-1], key = lambda x : x[0])[0]

print(solution(-10, -5, 5, 5, 1, [0, 0, 0, 0, 0, 1, 0]))