'''접근 방법
모서리에 있는 것은 방향이 바뀜
첫번째 좌표의 같은 행은 오른쪽으로 한 칸, 같은 열은 위로 한 칸
두번째 좌표의 같은 행은 왼쪽으로 한 칸, 같은 열은 밑으로 한 칸

모서리 4곳만 잘 신경써주면 됨! 왜냐! 거기서만 변환이 일어나고 덮어써질 수 있음

위치가 바뀌는 숫자들을 하나의 리스트로 모으고 min으로 출력
어떻게?
1. 규칙을 찾아서 값을 하나하나 이동해주려했음 -> 이렇게 하면 따로 저장해야할 부분이 많고 너무 헷갈림 -> 폐기


'''



# def solution(rows, columns, queries):
#     answer = []
#     matrix = []
#     temp = []

#     for i in range(1, columns*rows+1):
#         temp.append(i)
#         if len(temp) == columns:
#             matrix.append(temp)
#             temp = []

#     for query in queries:
#         # slice_mat = []
#         x1, y1 = query[0], query[1]
#         x2, y2 = query[2], query[3]
#         left_top =  matrix[x1-1][y1-1]
#         right_bot =  matrix[x2-1][y2-1]
#         for i in range(x2 - x1):
#             if i!= x2-x1-1:
#                 matrix[x1-1+i][y1-1] = matrix[x1+i][y1-1]
#                 matrix[x2-1-i][y2-1] = matrix[x2-1-i][y2-1]
#             else:
#                 matrix[x1-1+i][y1-1] = matrix[x1-1+i][y1]
#                 matrix[x2-1-i][y2-1] = matrix[x2-1-i][y2-2]

#             for j in range(y2 - y1 -1):
#                 if j == 0:
#                     matrix[x1-1][y1] = left_top
#                     matrix[x2-1][y2-2] = right_bot
#                 else:
#                     matrix[x1-1][y1+j+1] = matrix 


#         # sub_mat = matrix[x1-1:x2]
#         # for arr in sub_mat:
#         #     temp = arr[y1-1:y2]
#         #     slice_mat.append(temp)
            
#         # print(slice_mat)
#     return answer

'''접근방법2
테두리를 순서대로 돌면 되니까 그냥 시작포인트를 잡고 하나씩 돌아가는 식으로 진행
-> 코테에서 풀었던 아이디어 적용


'''

def solution(rows, columns, queries):
    answer = []
    matrix = []
    temp = []

    for i in range(1, columns*rows+1):
        temp.append(i)
        if len(temp) == columns:
            matrix.append(temp)
            temp = []

    for query in queries:
        x1, y1 = query[0]-1, query[1]-1
        x2, y2 = query[2]-1, query[3]-1
        dis1 = x2 - x1
        dis2 = y2 - y1
        dx = [0, 1, 0 ,-1]
        dy = [1, 0, -1, 0]

        stat = True
        idx = 0
        iter = 0
        temp = matrix[x1][y1]
        while stat:
            nx = x1 + dx[idx]
            ny = y1 + dy[idx]
            iter+=1

            matrix[nx][ny] = temp


            if iter == dis1:
                idx+=1
            elif iter == dis1+dis2:
                idx+=1
            elif iter == 2*dis1+dis2:
                idx+=1
            elif iter == 2*(dis1+dis2):
                idx+=1
                stat = False

            
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

solution(rows, columns, queries)