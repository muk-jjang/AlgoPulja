def solution(rows, columns, queries):
    answer = []
    # 문제 조건에 맞게 매트릭스 생성
    matrix=[[k*columns+i for i in range(1,columns+1)] for k in range(rows)]
    
    # 각 쿼리별 회전시키는 함수
    def rotate(querie):
        min_num=99999999
        start_row=querie[0]
        start_col=querie[1]
        end_row=querie[2]
        end_col=querie[3]
        prev=matrix[start_row-1][start_col-1]
        now=matrix[start_row-1][start_col-1]
        
        for col in range(start_col,end_col): #[2,3]부터 시작
            if prev<min_num:
                min_num=prev
            now=matrix[start_row-1][col] #기존 값 저장
            matrix[start_row-1][col]=prev # 값 변경
            prev=now #기존 값 prev로 저장
        
        # 아래로 내리는거 수행
        for row in range(start_row,end_row):
            if prev<min_num:
                min_num=prev
            now=matrix[row][end_col-1]
            matrix[row][end_col-1]=prev
            prev=now
            
        # 왼쪽으로 가는거 수행
        for col in range(end_col-2,start_col-2,-1): 
            if prev<min_num:
                min_num=prev
            now=matrix[end_row-1][col] #기존 값 저장
            matrix[end_row-1][col]=prev # 값 변경
            prev=now
        
        # 위로 가는거 수행
        for row in range(end_row-2,start_row-2,-1): 
            if prev<min_num:
                min_num=prev
            now=matrix[row][start_col-1] #기존 값 저장
            matrix[row][start_col-1]=prev # 값 변경
            prev=now
        
        return min_num
    
    for query in queries:
        answer.append(rotate(query))
    
    return answer
