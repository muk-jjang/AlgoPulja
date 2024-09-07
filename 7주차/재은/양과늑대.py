def dfs(n, info, graph, s=0, w=0):
    # n : 부모 노드
    max_s = 0
    for k in graph[n]:
        print(n)
        if info[n] == 0:
            s += 1
        else:
            w += 1
            if s == w:
                return s
        max_s = max(s,dfs(k, info, graph, s, w))
    # 리프노드일 경우
    # max, 현재 s값 비교
    return max_s


def solution(info, edges):
    # 방문 여부 고려 X
    # sheep : 양 개수
    # wolve : 늑대 개수
    # sheep == wolve -> -1, -1 후 return
    graph = [[] for _ in range(len(info))]
    # edge => graph reconstruct
    for e in edges:
        graph[e[0]].append(e[1])
    print(graph)
    answer = dfs(0, info, graph)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	))