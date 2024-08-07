'''
1주차 이모티콘이랑 매우 유사, 다만 가격 계산이 들어간다는점,, 이 아주 귀찮은거 하나 증가한듯?
'''
from math import ceil

def solution(fees, records):
    answer = []
    io_dic = {}
    fee_dic = {}
    time_limited = 23*60 + 59
    base_minute, base_fee, unit_minute, unit_fee = fees

    for record in records:
        time, number, io = record.split(' ')
        hour, minute = time.split(':')
        number = int(number)
        # print(hour, minute)

        time_cal =int(hour) * 60 + int(minute)
        # print(time_cal)
        if io == 'IN':
            io_dic[number] = time_cal
            fee_dic[number] = 0
        else:
            if time_cal-io_dic[number] > base_minute:
                fee_dic[number] += (base_fee + (ceil((time_cal - base_minute)/unit_minute)*unit_fee))
            else:
                fee_dic[number] += base_fee
            del io_dic[number]    

            
    for i, j in io_dic.items():
        if time_limited - j > base_minute:
            fee_dic[i] += (base_fee + (ceil((time_limited - base_minute)/unit_minute)*unit_fee))
        else:
            fee_dic[i] += base_fee
        


    sorted_list = sorted(fee_dic.items(), key = lambda x: x[0])
    print(sorted_list)
        

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution(fees, records)