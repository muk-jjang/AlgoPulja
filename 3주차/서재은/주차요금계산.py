import math
def time_calculate(i, o):
    # H 계산
    h = (int(o.split(':')[0]) - int(i.split(':')[0])) * 60
    # M 계산
    m = int(o.split(':')[1]) - int(i.split(':')[1])
    return h + m

def solution(fees, records):
    in_time = {}
    parked_acc = {}
    for log in records:
        time = log.split()[0]; number = log.split()[1]; status = log.split()[2]
        if number in in_time.keys():
            # in_time[number], time의 차 계산해서 parked_acc에 추가
            if number not in parked_acc.keys():
                parked_acc[number] = time_calculate(in_time[number], time)
            else:
                parked_acc[number] += time_calculate(in_time[number], time)
            in_time.pop(number)
        elif number not in in_time.keys():
            in_time[number] = time
    # 출차하지 않은 차들의 요금을 계산한다.
    for number,time in in_time.items():
        if number not in parked_acc.keys():
            parked_acc[number] = time_calculate(in_time[number], '23:59')
        else:
            parked_acc[number] += time_calculate(in_time[number], '23:59')

    answer = []
    for v in dict(sorted(parked_acc.items())).values():
        print(v)
        if int(v)>fees[0]:
            answer.append(fees[1] + math.ceil((int(v)-fees[0])/fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer