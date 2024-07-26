'''

HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, 
they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of  days, 
determine the number of times the client will receive a notification over all  days.

고객이 앞선 보낸 시간의 2배 이상 보내면 이상행동(잠재적으로 사기)으로 판단하고 경고
다만 전일 거래의 trailing number(최소 기준일)가 있을 때까지 경고를 보내지 않음



'''

import math
import os
import random
import re
import sys

# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d

''' 접근방법

DP 문제 같은데 흠 아 아니다 중간값이니까 DP 아니지! d가 짝수인 케이스랑 홀수인 케이스 나눠서 조져버리면 되네 
-> 홀수인 케이스는 그냥 중간값 -> 짝수인 케이스는 가운데 두 수의 평균
음... 일단 둘다 부분 리스트를 sorting 해야하네
근데 그래도 리스트를 처음부터 돌면 무조건 time limited 걸릴거 같은디... expenditure size가 2*10**5.. 그냥 돌면 시간 복잡도 n**2*d/2인가

새로 들어오는 값이 이전의 중간값보다 크냐 작냐? 
-> 크면은 앞선 리스트에서 max 값이 중간값, 작으면? 앞선 리스트에서 작은 값이랑 비교해봐야함
중간값 인덱스를 기억해놔야 할 거 같은데, 그래서 새로 들어오는 값을 마지막 인덱스랑 비교하고 
-> 근데 이렇게 해도 결국 똑같은디

부분 sort 해도 최악의 경우 n**2로그n, for문을 한번만 돌면 좋을텐디 -> 그러려면 위에 접근이 맞는거 같은데

'''
def activityNotifications(expenditure, d): #expenditure size n
    init_list = expenditure[0 : d]
    
    init_list.sort()
    # if d % 2 == 0:
    #     median = (init_list[d/2] + init_list[d/2 -1] )
    # else: 
    #     median = init_list[d//2]
    
    median_index = 

    for i in range(d , len(expenditure)-d):
        # if expenditure[i] > median

    
    return