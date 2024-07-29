def solution(s):
    length=len(s)
        
    # 1부터 길이의 절반까지 스플릿 진행
    words=[]
    answers=[]
    # 테스트케이스 5번에서 에러뜬 이유가 글자가 하나인 경우 아래 range(1,int(length//2)+1)에서 빈 값이 리턴되어 최종 답도 빈 값으로 출력되기떄문, 한 글자의 경우 바로 answer=1
    if length==1:
        return 1
    else:
        for l in range(1,int(length//2)+1):
            words=[]
            i=0
            while True:
                if (i+l)>length:
                    words.append(s[i:])
                    break
                else:
                    words.append(s[i:i+l])
                i+=l

            # count시작
            prev=''
            count=1
            result=''

            for word in words:
                # 중복인 경우
                if prev==word:
                    count+=1
                # 중복이 아닌 경우
                else:
                    # 기존에 중복이 있는 경우
                    if count>1:
                        result=result+str(count)+prev
                        prev=word
                        count=1
                    # 기존에 중복이 없는 경우
                    else:
                        result=result+prev
                        prev=word
            # 마지막 남은거 추가
            if count>1:
                result=result+str(count)+prev
            else:
                result=result+prev

            answers.append(len(result))


        answer=min(answers)
        return answer
