def validate(place):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for x in range(5):
        for y in range(5):
            if place[x][y]!='P':
                continue
            for _ in range(4):
                nx = x + dx[_]; ny = y + dy[_]
                if 0 <= nx <5 and 0 <= ny < 5:
                    if place[nx][ny] == 'P':
                        return 0
                    if place[nx][ny] == 'X':
                        pass
                    if place[nx][ny] == 'O':
                        for k in range(4):
                            if 0<=(ny+dy[k])<5 and 0<=(nx+dx[k])<5 and (nx+dx[k],ny+dy[k])!=(x,y):
                                if place[nx+dx[k]][ny+dy[k]]=='P':
                                    return 0

    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(validate(place))
          
    return answer