import numpy as np
import itertools

def convert(board):
    return list(itertools.chain(*board))

def operation_2(board,skill,N):
    a,b,c,d = map(int,skill[1:5])
    degree = skill[-1]
    if skill[0]==1:
        for i in range(a,c+1):
            for j in range(b,d+1):
                board[i*N+j] -= degree
    elif skill[0]==2:
        for i in range(a,c+1):
            for j in range(b,d+1):
                board[i*N+j] += degree
    return board

def operation(board,skill):
    a,b,c,d = map(int,skill[1:5])
    degree = skill[-1]
    # 공격
    if skill[0]==1:
        for i in range(a,c+1):
            for j in range(b,d+1):
                board[i][j] -= degree
    # 회복
    elif skill[0]==2:
        for i in range(a,c+1):
            for j in range(b,d+1):
                board[i][j] += degree
    return board

'''
최종 코드
'''

def skill_operation(skill, N, M):
    # N*M matrix에 skill의 영향을 받은 최종 skill map을 저장한다.
    tmp = [[0] * (M+1) for _ in range(N+1)]
    for s in skill:
        type = s[0]
        a,b,c,d = map(int,s[1:5])
        degree = s[-1]
        if type==2 : degree = -degree
        tmp[a][b] -= degree
        tmp[a][d+1] += degree
        tmp[c+1][b] += degree
        tmp[c+1][d+1] -= degree
    
    for i in range(N+1):
        for j in range(M):
            tmp[i][j+1] += tmp[i][j]
            
    for j in range(M+1):
        for i in range(N):
            tmp[i+1][j] += tmp[i][j]
    return tmp
        
def solution(board, skill):
    N = len(board); M = len(board[0])
    answer = 0
    #board = convert(board)
    skill_map = skill_operation(skill, N, M)
    for i in range(N):
        for j in range(M):
            board[i][j] += skill_map[i][j]
            if board[i][j]>0: answer += 1
    return answer