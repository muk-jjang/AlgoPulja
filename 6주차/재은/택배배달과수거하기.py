def solution(cap, n, deliveries, pickups):
    answer = 0
    # 택배의 수거, 배달을 스택으로 처리
    d_stack = []
    p_stack = []
    for i in range(n):
        if deliveries[i] != 0:
            d_stack.append(i)
        if pickups[i] != 0:
            p_stack.append(i)

    remain = cap
    while p_stack or d_stack:
        d_dist = d_stack[-1]+1 if d_stack else 0
        p_dist = p_stack[-1]+1 if p_stack else 0
        remain = cap
        
        while d_stack and remain > 0:
            idx = d_stack.pop(-1)
            if deliveries[idx] <= remain :
                remain -= deliveries[idx]
            else:
                deliveries[idx] -= remain
                d_stack.append(idx)
                break
        
        remain = cap
        while p_stack and remain > 0:
            idx = p_stack.pop(-1)
            if pickups[idx] <= remain :
                remain -= pickups[idx]
            else:
                pickups[idx] -= remain
                p_stack.append(idx)
                break

        answer += 2 * max(d_dist, p_dist)
    return answer

print(solution(2,7,[1,0,2,0,1,0,2],[0,2,0,1,0,2,0]))