'''접근방법
생성 정점 -> 나가는 간선 수 = 그래프 수, 나가는 엣지만 존재
도넛 ->  본인으로 들어오는 간선 1개이지만, cycle이 생성돼야함
막대 -> 본인으로 들어오는 간선만 존재
8자 -> 중앙 노드에 들어오는 간선 두 개 이상, 나가는 간선 두 개

edge의 길이가 100만개, 완전탐색은 어려움

'''

def solution(edges):
    answer = [0, 0, 0, 0]
    last = max(map(max,edges))
    graph_num = 0
    in_edge, out_edge = [0] * last, [0] * last

    # 노드마다 나가는 간선 들어오는 간선 카운트
    for out_c, in_c in edges:
        out_edge[out_c] += 1
        in_edge[in_c] += 1

    # 각 그래프 조건 확인
    for i in range(1, last):
        if in_edge[i] == 0 and out_edge[i] >= 2: # 생성된 노드
            answer[0] = i
            graph_num = out_edge[i]
        elif in_edge[i] >= 1 and out_edge[i] == 0: # 막대
            answer[1] += 1
        elif in_edge[i]>=2 and out_edge[i] == 2: # 8자
            answer[3]+= 1

    answer[2] = graph_num - (answer[1] + answer[3]) #도넛 -> 전체그래프 수에서 다른 그래프 수 제외
      
    return answer

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]

# print(max(map(max,edges)))