'''접근방법
userid로 구분하고 user들의 행동로그는 최대 100000
use가 취하는 행동은 Enter, Leave, Change중 하나

change, Enter가 있었는지 아닌지만 파악하고 있으면 됨
처음 들어왔을 때 userid랑 이름을 dic형태로 저장하고
change, Enter가 있었을 때 해당 유저 이름 변경 , 근데 Enter,Change는 user의 이름까지 표기해줌 -> 그러므로 문장이 세단어로 표현

'''
'''해당 문제의 핵심은 
1. userid를 기준으로 판단하면 유니크한 유저를 볼 수 있다는 것
2. user의 행동로그 최대값을 보고 dic형태를 생각해내는 것(빠른 탐색을 위해)
3. Enter, Change에서의 문자열 길이를 보고 user의 이름이 바뀔 수 있는 경우를 체크하는 것
'''

def solution(record):
    user_dic = {}
    answer = []
    for log in record:
        log_list = log.split() # 문장 자르기

        if len(log_list) == 3: #change랑 enter에는 유저의 이름이 기입됨  -> 길이가 3인 경우
            user_dic[log_list[1]] = log_list[2] 
            # 유저의 아이디에 맞는 이름을 dic 형태로 저장 -> 이름을 바꿀 수 있는 경우가 2가지가 있음 나갔다 들어오거나 이름을 변경하거나
            # 결국 들어오든 변경하든 두 가지 케이스라면 마지막에 변경된 이름만 기억하면 됨

    for log in record: # log에서 입장이거나 떠나는 케이스만 구분 -> 채팅 기록에 남음
        log_list = log.split()
        if log_list[0] == "Enter": # 해당 두 케이스일 때 userid dic에서 해당 유저의 이름을 가지고 옴
            answer.append(user_dic[log_list[1]]+"님이 들어왔습니다.")
        elif log_list[0] == "Leave":
            answer.append(user_dic[log_list[1]]+"님이 나갔습니다.")
    return answer # 시간복잡도 2n 

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

solution(record)