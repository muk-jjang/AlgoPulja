def solution(n, build_frame):
    # 상태 저장 - answer의 형식으로 저장
    # 설치 시 예외처리
    # 삭제 시 예외처리
    state = []
    def install_gi(action,state):
        # 좌표
        xy=action[:2]
        # 1) 땅바닥이거나 2)아래에 보가 있거나 3)기둥 위이기만 하면됨
        if (action[1]==0) or ([xy[0]-1,xy[1],1] in state) or ([xy[0],xy[1],1] in state) or ([xy[0],xy[1]-1,0] in state):
            state.append(action[:3])
        return state
            
    def install_bo(action,state):
        xy=action[:2]
        
        if xy[1]>0:
            # 1)한쪽에 기둥이 있거나 2) 두 쪽이 보에 연결되어있는 경우
            if ([xy[0],xy[1]-1,0] in state) or ([xy[0]+1,xy[1]-1,0] in state) or ([xy[0]-1,xy[1],1] and [xy[0]+1,xy[1],1] in state):
                state.append(action[:3])
        return state
            
    def delete_gi(action,state):
        xy=action[:2]
        
        # 1)기둥 위의 보가 한쪽이 연결이 없어지는 경우, 2)위에 기둥이 연결이 없어지는 경우
        # 해당 기둥과 연결된 구조물의 안정성 체크
        stable = 1
        if not ([xy[0],xy[1]+1,1] and [xy[0]-1,xy[1]+1,1]):
            if [xy[0],xy[1]+1,1] in state: # 오른쪽 보 안정성 체크
                if [xy[0]+1,xy[1],0] not in state:
                    if [xy[0]+1,xy[1]+1,1] not in state:
                        stable=None

            elif [xy[0]-1,xy[1]+1,1] in state: # 왼쪽 보 안정성 체크
                if [xy[0]-1,xy[1],0] not in state:
                    if [xy[0]-2,xy[1]+1,1] not in state:
                        stable=None
            if [xy[0],xy[1]+1,0] in state: # 기둥이 있는 경우
                if ([xy[0]-1,xy[1]+1,1] not in state) and ([xy[0],xy[1]+1,1] not in state):
                    stable=None
        if stable:
            state.remove(action[:3])
        return state

        
    def delete_bo(action,state):
        #1)보 위에 기둥이 있거나 2)인접 보가 불안정해질경우
        xy=action[:2]
        stable=1
        # 기둥 쳌
        if [xy[0],xy[1]+1,0] in state: #왼쪽 기둥
            if ([xy[0]-1,xy[1],1] not in state) and ([xy[0],xy[1]-1,0] not in state):
                stable=None
        if [xy[0]+1,xy[1]+1,0] in state: #오른쪽 기둥
            if ([xy[0]+1,xy[1],1] not in state) and ([xy[0]+1,xy[1]-1,0] not in state):
                stable=None
        # 왼 보 쳌
        if [xy[0]-1,xy[1],1]:
            if ([xy[0],xy[1]-1,0] not in state) and ([xy[0]-1,xy[1]-1,0] not in state):
                stable=None
        # 오 보 쳌
        if [xy[0]+1,xy[1],1]:
            if ([xy[0]+1,xy[1]-1,0] not in state) and ([xy[0]+2,xy[1]-1,0] not in state):
                stable=None
        if stable:
            state.remove(action[:3])
        return state
        
        
    for action in build_frame:
        if action[-2]==0: #기둥에 대한 작업
            if action[-1]==0: # 기둥 삭제
                delete_gi(action,state)
            else: #기둥 설치
                install_gi(action,state)
                
        else: #보에 대한 작업
            if action[-1]==0: # 보 삭제
                delete_bo(action,state)
            else:
                install_bo(action,state)
            
    state.sort()
    return state
