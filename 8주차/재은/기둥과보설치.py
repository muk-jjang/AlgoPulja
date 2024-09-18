def solution(n, build_frame):
    # 구조물들만 저장해두는 리스트를 생성하고, 좌표로 검증한다.
    # 리스트 : (x, y, a) 튜플이 저장된 리스트
    frames = []
    # 함수 is_available : 현재 설치/삭제하려는 구조물이 지지 가능한지 확인한다.
    # result에 들어있는 구조물들을 이용해 검증한다.
    def is_available(build, frames):
        x, y, a = map(int, build)
        # 기둥
        if a == 0:
            if y == 0 or (x, y-1, 0) in frames or (x-1,y,1) in frames or (x, y, 1) in frames:
                return True
        if a == 1:
            if (x,y-1,0) in frames or (x+1,y-1,0) in frames or ((x-1,y,1) in frames and (x+1,y,1) in frames):
                return True
        return False
    
    for cur in build_frame:
        if cur[3] == 1:
            if is_available(tuple(cur[:-1]), frames):
                frames.append(tuple(cur[:-1]))
                
        else:
            if tuple(cur[:-1]) in frames:
                frames.remove(tuple(cur[:-1]))
                for test in frames:
                    if not is_available(test, frames):
                        frames.append(tuple(cur[:-1]))
                        break
                          
    answer = sorted(frames)
    return answer