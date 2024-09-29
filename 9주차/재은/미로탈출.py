# 경로에도 우선순위가 있다. (down - left - right - up)
# DFS로 그래프 접근 ??
# 열 접근 == dx / 행 접근 == dy
# graph[y][x] 이렇게 접근해야됨

dx = [1,0,0,-1]
dy = [0,-1,1,0]
direction = 'dlru'
flag = False

def possible(n,m,x,y,r,c,k):
    dist = abs(x-r) + abs(y-c)
    if dist > k:
        return False
    elif dist == k:
        return True
    else:
        if (k-dist)%2==0:
            return True
        return False

def dfs(x,y,n,m,r,c,k,path):
    global flag
    result = 'impossible'
    if not flag:
        for i in range(4):
            nx = dx[i] + x; ny = dy[i] + y
            # nx, ny 가능 확인
            if not (1 <= nx <= n and 1 <= ny <= m):
                continue
            if len(path) == k:
                if r == x and c == y:
                    flag = True
                    return path
            if len(path) < k :
                result = dfs(nx,ny,n,m,r,c,k,path+direction[i])
                if flag:
                    break
    return result

def solution(n, m, x, y, r, c, k):
    answer = ''
    if not possible(n,m,x,y,r,c,k):
        answer = 'impossible'
    else:
        answer = dfs(x,y,n,m,r,c,k,path='')
    return answer