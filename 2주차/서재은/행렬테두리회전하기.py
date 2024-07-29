graph = []
def rotate(x_min, y_min, x_max, y_max):
    global graph
    x_min -= 1; y_min -=1; x_max -=1; y_max -=1
    # x_min : 행 시작, y_min : 열 시작
    # graph[x][y]로 접근
    graph_tmp = [item[:] for item in graph]
    min_result = 10001
    # 행 고정 열 변경
    y = y_min
    while y < y_max:
        graph_tmp[x_min][y+1] = graph[x_min][y]
        min_result = min(graph_tmp[x_min][y+1], min_result)
        y += 1
    # 열 고정 행 변경
    x = x_min
    while x < x_max:
        graph_tmp[x+1][y_max] = graph[x][y_max]
        min_result = min(graph_tmp[x+1][y_max], min_result)
        x += 1
    # 행 고정 열 변경
    y = y_max
    while y > y_min:
        graph_tmp[x_max][y-1] = graph[x_max][y]
        min_result = min(graph_tmp[x_max][y-1], min_result)
        y -= 1
    # 열 고정 행 변경
    x = x_max
    while x > x_min:
        graph_tmp[x-1][y_min] = graph[x][y_min]
        min_result = min(graph_tmp[x-1][y_min], min_result)
        x -= 1
    graph = graph_tmp
    return min_result
    
def solution(rows, columns, queries):
    for i in range(rows):
        graph.append([i*columns + j for j in range(1,columns+1)])
    answer = []
    for q in queries:
        answer.append(rotate(*q))
    return answer

if __name__ == '__main__':
    print(solution(5,5,[[2, 3, 4, 5], [2, 3, 4, 5], [2, 3, 4, 5], [2, 3, 4, 5]]))