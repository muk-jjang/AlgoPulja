# 유저는 아이디로 식별
# {유저 : 닉네임} 딕셔너리 외부에 선언 -> 안정성 있는 코드를 위해서는 글로벌 변수를 어떻게 관리할 수 있을까 고민고민 ,,,
users = {}

def message(msg):
    msg = msg.split()
    # 0 : 들어옴, 1 : 나감
    if msg[0] == 'Enter':
        users[msg[1]] = msg[2]
        # 어차피 최종 출력값은 마지막 닉네임임
        return (msg[1], 0)
    elif msg[0] == 'Leave':
        return (msg[1], 1)
    elif msg[0] == 'Change':
        users[msg[1]] = msg[2]
        return

def solution(record):
    answer_tmp = []
    for r in record:
        result = message(r)
        try:
            if result[1] == 0:
                answer_tmp.append(result[0] + " 0")
            elif result[1] == 1:
                answer_tmp.append(result[0] + " 1")
        except:
            pass
    answer = []
    for a in answer_tmp:
        msg = "님이 들어왔습니다." if a.split()[1]=="0" else "님이 나갔습니다."
        answer.append(users[a.split()[0]] + msg)
    return answer