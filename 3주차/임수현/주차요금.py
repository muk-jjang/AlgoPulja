def solution(fees, records):
    basic_time,basic_fee,unit_time,unit_fee=fees
    
    dic={}
    
    for record in records:
        time,car_num,state = record.split(' ')
        t = time.split(':')
        hour=int(t[0])
        minute=int(t[1])
        
        if car_num in dic.keys():
            dic[car_num].append(hour)
            dic[car_num].append(minute)
        else:
            dic[car_num]=[hour,minute]

    car_numbers=sorted(dic.keys())
    answer=[]
    
    for car_number in car_numbers:
        # 출차 정보까지 있는 경우
        value=dic[car_number]
        
        # 최종 풀차 정보가 없는 경우
        if len(value)%4!=0:
            value.append(23)
            value.append(59)
        
        minutes=0
        bit=-1
        for h in range(0,len(value),2):
            minutes+=bit*value[h]*60
            bit=bit*(-1)
        bit=-1
        for m in range(1,len(value),2):
            minutes+=bit*value[m]
            bit=bit*(-1)
        
        # 요금 계산
        if minutes<=basic_time:
            answer.append(basic_fee)
        elif minutes>basic_time:
            count = int((minutes-basic_time)//unit_time)
            if (minutes-basic_time)%unit_time!=0:
                count+=1
            total = count*unit_fee+basic_fee
            answer.append(total)
    return answer