def solution(record):
    answers=[]
    result=[]
    # uid와 닉네임을 쌍으로 저장하기 위한 dic제작
    nickname_dic={}
    # 상황별로 조건 수행
    for re in record:
        words = re.split()
        
        if words[0]=='Enter':
            answers.append([words[1],'님이 들어왔습니다.'])
            nickname_dic[words[1]]=words[2]
        if words[0]=='Leave':
            answers.append([words[1],'님이 나갔습니다.'])
        if words[0]=='Change':
            nickname_dic[words[1]]=words[2]
    # uid를 닉네임으로 변경하여 최종 출력 제작
    for answer in answers:
        nickname=nickname_dic[answer[0]]
        sentence = nickname+answer[1]
        result.append(sentence)
        
    return result
