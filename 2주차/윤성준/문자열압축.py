'''접근방법
문자열 길이 1 ~ 1000 -> 1부터 1000까지 다 슬라이싱 해보는 것은?, 문자열 처음부터 슬라이싱 해야하기 때문에 나쁜 방법은 아닌듯함
처음부터 슬라이싱 하는 것이라면 애초에 최대로 슬라이싱 할 수 있는 것은 500!
그리고 약수로만 슬라이싱 가능?한게 맞나? 근데 약수로만 슬라이싱 하여 계산하면 엄청 쉬운 문제인듯? 
어차피 길이만 출력하는 것이기 때문에 슬라이싱 하고 set으로 바꾸면 얼만큼 줄어드는지는 확인 가능


'''
# 방법 1 -> 잘못 생각
# def solution(s):
#     sentence_len = len(s)
#     divisors = []
#     answer_dic = {}
#     answer = 0
#     for i in range(1, sentence_len):
#         if sentence_len % i ==0 :
#             divisors.append(i)

#     for divisor in divisors:
#         start = 0
#         end = divisor
#         sentence_list = []
#         stat = True
#         while stat:
#             sentence_list.append(s[start: end])
#             start += divisor
#             end += divisor
#             if end > sentence_len:
#                 stat = False
#                 sentence_set = set(sentence_list)
#                 for item in sentence_set:
    #                 answer_dic[item] = sente


    # return answer

'''접근방법 2 -> 이거 내가 푼거 아님
슬라이싱으로 하나하나 접근할 수 있는 이유는 문자열 최대 길이가 1000
1. 약수를 구한다? -> 슬라이싱 했을 때 끝에 나눠떨어지지 않는 것을 대비
2. sentence처음부터 약수만큼 슬라이싱 하여, 다음 슬라이싱 된 값과 비교한다
3. 두 개가 같으면 count를 하고 다르면 다음 슬라이싱 된 것을 비교 값으로 넣어준다, -> count가 1보다 크면 압축이 가능하므로 앞에 count만큼 더해준다
4. count가 1보다 작으면 result에 그냥 temp만 더해줌
5. 마지막 슬라이싱을 고려해주지 못 하므로 for문을 다 돌고 나왔을 때, count가 1보다 큰지 아닌지를 확인하고 result에 더해준다

!! answer는 따로 리스트 만들 필요없이, min함수 통해서 업데이트
'''

def solution(s):
    answer = 1000
    sentence_len = len(s)
    # divisors = []
    # for i in range(1, sentence_len):
    #     if sentence_len % i ==0 :
    #         divisors.append(i)

    for divisor in range(1, sentence_len+1): # 0~ 1000까지 슬라이싱 돌겠다
        count = 1
        temp = s[0:divisor] # 맨 처음 비교할 슬라이싱 값
        result = "" # 결과값 저장
        for i in range(divisor,len(s),divisor):
            if temp == s[i:i+divisor]: # 다음 슬라이싱이랑 같으면 카운팅
                count+=1
            else: 
                if count > 1: # 달랐을 때 count >1 이면 연달아 중복 됨 -> 압축가능
                    result += str(count) + temp
                    temp = s[i:i+divisor]
                    count = 1
                else:
                    result += temp
                    temp = s[i:i+divisor]
                    count = 1
        if count > 1: # 마지막 슬라이싱 고려
            result += str(count) + temp
        else : 
            result += temp
        answer = min(answer, len(result)) # min을 통해서 answer 업데이트
                
    return answer

s = "ababcdcdababcdcd"

print(solution(s))

'''
상윤 조언
'''

def solution(s):
    answer = 1000
    sentence_len = len(s)
    # divisors = []
    # for i in range(1, sentence_len):
    #     if sentence_len % i ==0 :
    #         divisors.append(i)

    for divisor in range(1, sentence_len+1):
        count = 1
        temp = s[0:divisor]
        result = ""
        for i in range(divisor,len(s),divisor):
            if temp == s[i:i+divisor]:
                count+=1
            else: 
                if count > 1:
                    result += str(count) 

                result += temp
                temp = s[i:i+divisor]
                count = 1    

        if count > 1:    
            result += str(count) 

        result += temp
        answer = min(answer, len(result))
                
    return answer