# 브루트포스처럼 단위 1씩 늘려가기
# prev 저장해두고 이후 [:n]이 동일하면 묶음

def split_str(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def compression(s, n):
    sliced = split_str(s, n)
    # 마지막 문자열과의 비교를 위해 0 추가
    sliced.append(0)
    k = 1
    result = []
    for i in range(len(sliced)-1):
        prev = sliced[i]
        now = sliced[i+1]
        if prev == now:
            k += 1
        else:
            result.extend([k,prev])
            k = 1
    # 한 번만 반복되는 경우 고려해서 1 제거
    while 1 in result:
        result.remove(1)
    result = "".join(map(str,result))
    return len(result)

def solution(s):
    n = 1
    answer = []
    while n < len(s)+1:
        answer.append(compression(s,n))
        n += 1
    return min(answer)

