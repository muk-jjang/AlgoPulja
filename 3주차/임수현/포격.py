def solution(board, skill):
    row=len(board)
    col=len(board[0])
    
    # skill = sorted(skill, key=lambda x : x[0])
    attacks = []
    heals=[]
    # 공격 회복 분리
    total_heal=0
    for sk in skill:
        if sk[0]==1:
            attacks.append(sk)
        else:
            heals.append(sk)
            total_heal+= sk[-1]
    # 공격 시작
    for attack in attacks:
        for r in range(attack[1],attack[3]+1):
            for c in range(attack[2],attack[4]+1):
                board[r][c]-=attack[-1]
    
    destory=[]
    count=0
    for r in range(row):
        for c in range(col):
            if board[r][c]<=0:
                if -board[r][c]<=total_heal:
                    destory.append([r,c])
            else:
                count+=1
    if len(destory)==0:
        return count

    for r,c in destory:
        for heal in heals:
            if heal[1]<=r<=heal[3] and heal[2]<=c<=heal[4]:
                board[r][c]+=heal[-1]
                if board[r][c]>0:
                    # destory.remove([r,c])
                    count+=1
    return count