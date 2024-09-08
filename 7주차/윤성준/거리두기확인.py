'''접근 방법
앉은 자리의 인덱스만 뽑고 인덱스끼리의 맨하튼 거리를 구한다.
맨하튼 거리가 2이하인 부분들만 사이 인덱스에 파티션이 있는지 체크?
-> 이렇게 단순 생각으로 가능한 이유는 5*5의 제한적인 상황이기 때문에, 시간복잡도 측면에서 문제가 없어보임
-> 앉아있는 사람을 중앙에 두고 3*3의 크기만 계속 확인하면 됨
-> 근데 이렇다면 애초에 3*3의 크기로 컨볼루션 돌듯이 다 돌아봐도 될듯?
-> 위 아래 옆 패딩으로 빈자리를 두고 3*3 컨볼루션 느낌으로 돌고 -> 가능한지 확인


'''
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(candidate, place): # candidate는 'P'
    queue = deque()
    visited = [[False]*5 for _ in range(5)]
    queue.append(candidate)
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if visited[nx][ny]:
                continue
            if place[nx][ny] == 'X':
                continue
            if place[nx][ny] == 'P':
                return False
            queue.append((nx, ny))
        
        cnt += 1
        if cnt == 2:
            return True
    return True
            

def solution(places):
    answers = []
    

def solution(places):
    answer = []
    return answer