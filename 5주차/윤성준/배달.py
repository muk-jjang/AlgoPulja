'''접근방법
최단경로 알고리즘중 다익스트라 사용
시작노드를 기준으로 각 노드로 가는 최단경로 업데이트
1. 출발 노드 설정
2. 출발 노드를 기준으로 각 노드의 최소 비용 저장
3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택
4. 해당 노드를 거쳐서 특정한 노드로 가는 경우 고려하여 최소비용 갱신
3~4 반복
'''
import heapq as hq


def solution(N, road, K):
    answer = 0
    adj = [[1e6]*(N+1) for _ in range(N+1)]
    
    for a, b, c in road:
        adj[a][b] = min(adj[a][b], c)
        adj[b][a] = min(adj[b][a], c)
    
    # 해당 노드까지 가는데 최단거리
    dis = [1e6] * (N+1)
    dis[1] = 0

    # min-heap으로 노드까지의 거리 저장, 
    heap = []
    hq.heappush(heap, (dis[1], 1))

    while heap:
        cost, cur_node = hq.heappop(heap)
        
        # 저장된 거리가 cost보다 적으면 다음으로
        if dis[cur_node] < cost:
            continue
        
        for i in range(1, N+1):
            if dis[i] > cost + adj[cur_node][i]:
                dis[i] = cost + adj[cur_node][i]
                hq.heappush(heap, (dis[i], i))

    for i in range(1, N+1):
        if dis[i] <= K:
            answer += 1       
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

print(solution(N, road, K))